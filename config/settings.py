#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/13 17:28
@File: settings.py
@IDE: PyCharm
@Description: 
"""
import os
from pathlib import Path


# 项目根目录
ROOT_DIR = Path(__file__).parent.parent
LOGS_DIR = ROOT_DIR / "logs"
REPORTS_DIR = ROOT_DIR / "reports"
SCREENSHOTS_DIR = ROOT_DIR / "screenshots"
IMAGES_DIR = Path(__file__).parent.parent / "statics" / "images"
NGINX_DIR = ROOT_DIR / "nginx-1.29.0"

# 创建必要目录
for dir_path in [LOGS_DIR, REPORTS_DIR, SCREENSHOTS_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# 设备配置（支持多设备）
DEVICE_CONFIG = {
    "android": {
        "platform": "Android",
        "uuid": None,  # 留空则自动连接第一个设备
        "cap_method": "JAVACAP",  # 图像截取方式
        "touch_method": "ADBTOUCH",
    }
}

# 环境切换
ENV = "stage"  # dev / test / staging / prod / stage

# API 配置
API_BASE_URLS = {
    "stage": "https://first.stage.core.vivalink.com",
    "test": "https://first.stage.core.vivalink.com",
}

API_BASE_URL = API_BASE_URLS[ENV]
API_TIMEOUT = 30


# 超时配置
WAIT_TIME = 10          # 隐式等待/元素等待超时（秒）
POLL_FREQ = 0.5         # 轮询间隔

# 报告配置
REPORT_TITLE = "Airtest Android 自动化测试报告"
REPORT_HTML = REPORTS_DIR / "report.html"

# 日志配置
LOG_LEVEL = "INFO"
LOG_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d]->%(levelname)s: %(message)s'
LOG_MODE= "a"






# 零时服务端口
Port = "8111"

# API base URL
API_BASE_URL = "https://first.stage.core.vivalink.com"

# Allure Report
def get_section_ALLURE_REPORT_CUSTOM(custom):

    customs = {
        "title": "Vivalink Webportal Report",
        "LogoFile": "./statics/imgs/favicon.ico",
        "reportFilePath": "./reports/allure_reports_html",
        "allureFilePath": "./allure-2.29.0",
        "allureResultsPath": "./reports/allure_reports",
        "logoText": "Report",
        "reportContentTitle": "WebPortal v2.7 Report",
        "BaseUrl": API_BASE_URL
    }

    allure_report_custom = customs[custom]

    return allure_report_custom