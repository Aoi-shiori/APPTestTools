#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/13 17:35
@File: run.py
@IDE: PyCharm
@Description: 测试入口，整合 pytest、Allure、Nginx 报告服务
"""
import pytest
import sys
import os
from config.settings import REPORTS_DIR
from utils.allureUtil import allureUtil
from utils.nginx import Nginx
from utils.logger import get_logger

logger = get_logger(__name__)

if __name__ == "__main__":
    """ 
    支持的 pytest 参数说明：
    -v (Verbose)：输出详细信息
    -s (Stdout)：显示 print 输出
    -k [表达式]：匹配用例名称关键字
    -m [标记名]：执行被 @pytest.mark.[标记名] 标记的用例
    -n [线程数]：并发运行（需 pytest-xdist）
    --lf：只重新运行上一次失败的用例
    --ff：优先运行失败的用例
    --collect-only：仅收集用例，不执行
    """

    # 1. 定义基础参数（可根据需要动态扩展）
    args = [
        "tests",                        # 测试目录
        "-v",                           # 详细输出
        "-s",                           # 打印控制台输出
        "--alluredir=./reports/allure_reports",   # Allure 原始数据目录
        "--clean-alluredir",            # 运行前清空该目录
        f"--html={REPORTS_DIR}/report.html",      # pytest-html 报告
        "--self-contained-html",        # 独立 HTML 文件
        "--maxfail=3",                  # 失败 3 次后停止
    ]

    # 2. 支持从命令行传入额外参数（例如：python run.py -m smoke）
    # 提取 sys.argv 中不属于脚本自身的参数，追加到 args
    extra_args = [arg for arg in sys.argv[1:] if not arg.startswith("--capture")]
    args.extend(extra_args)

    # 3. 准备 Allure 环境（替换配置文件等）
    allure = allureUtil()
    allure.replaceAllureconfig()

    # 4. 开始执行测试
    logger.info(f"{'*' * 20} 开始执行测试用例 {'*' * 20}")
    exit_code = pytest.main(args)       # 只运行一次，使用完整的 args

    # 5. 根据执行结果记录日志
    if exit_code == 0:
        logger.info("所有测试用例执行通过")
    else:
        logger.error(f"测试执行失败，退出码: {exit_code}")

    # 6. 生成 Allure HTML 报告
    logger.info("正在生成 Allure HTML 报告...")
    allure_generate_cmd = "allure generate ./reports/allure_reports -o ./reports/allure_reports_html --clean"
    os.system(allure_generate_cmd)

    # 7. 自定义 Allure 报告（添加环境信息、分类等）
    allure.doAllureCustom()   

    # 8. （可选）启动 Nginx 服务托管报告
    # 注意：Nginx 类的 dosomething() 应实现启动/重载服务逻辑
    try:
        nginx = Nginx()
        nginx.dosomething()
        logger.info("Nginx 报告服务已启动")
    except Exception as e:
        logger.warning(f"Nginx 服务启动失败: {e}")

    logger.info(f"{'*' * 20} 测试用例执行完成 {'*' * 20}")

    # 9. 返回退出码（供 CI/CD 判断）
    sys.exit(exit_code)
