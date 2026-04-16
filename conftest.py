#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/13 17:33
@File: conftest.py
@IDE: PyCharm
@Description: 
"""
import pytest
from core.device_manager import device_mgr
from core.base_page import BasePage
from airtest.core.api import set_current, G
import time

@pytest.fixture(scope="session", autouse=True)
def connect_device():
    """整个测试会话连接一次设备"""
    device_mgr.connect()
    yield
    device_mgr.disconnect()

@pytest.fixture
def base_page():
    """每个测试用例前的页面基类实例"""
    page = BasePage()
    # 可选：等待应用就绪
    time.sleep(2)
    yield page
    # 用例后清理（可选）
    pass

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """测试失败时自动截图"""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        # 获取当前页面对象截图
        try:
            from core.base_page import BasePage
            bp = BasePage()
            screenshot_path = bp.take_screenshot(name=f"{item.name}_failed")
            # 将截图路径添加到报告
            if hasattr(rep, 'extra'):
                rep.extra = getattr(rep, 'extra', [])
                rep.extra.append(screenshot_path)
        except Exception as e:
            print(f"截图失败: {e}")