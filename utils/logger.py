#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/13 17:28
@File: logger.py
@IDE: PyCharm
@Description: 
"""

import logging
from config.settings import LOGS_DIR, LOG_LEVEL, LOG_FORMAT,LOG_MODE
import sys

def get_logger(name="AirtestFramework"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(LOG_LEVEL)
        # 文件处理器
        fh = logging.FileHandler(LOGS_DIR / "test.log", encoding="utf-8", mode=LOG_MODE)
        fh.setLevel(LOG_LEVEL)
        # 控制台处理器
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(LOG_LEVEL)
        # 格式化
        formatter = logging.Formatter(LOG_FORMAT)

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        # ----- 关键：将同一个 FileHandler 也添加到 airtest 的 logger -----
        airtest_logger = logging.getLogger('airtest')  # airtest 使用的 logger 名称通常是 'airtest'
        # 避免重复添加相同的 handler（可选，但推荐）
        if fh not in airtest_logger.handlers:
            airtest_logger.addHandler(fh)
        # 同时设置级别，避免过多 debug 日志
        airtest_logger.setLevel(LOG_LEVEL)  # 或 logging.WARNING 以减少输出

        # 如果 airtest 还有使用其他 logger 名称（如 'airtest.core'），可以一并添加
        # 但通常设置 'airtest' 就足够了，因为子 logger 会传播
    return logger