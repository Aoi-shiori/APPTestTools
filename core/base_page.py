#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/13 17:30
@File: base_page.py
@IDE: PyCharm
@Description: 
"""
from airtest.core.api import touch, swipe, exists, Template, snapshot, keyevent
from airtest.core.api import G
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from config.settings import WAIT_TIME, SCREENSHOTS_DIR
from utils.logger import get_logger
import time

logger = get_logger()

class BasePage:
    def __init__(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        self.wait_time = WAIT_TIME

    def tap_element(self, selector, selector_type="poco"):
        if selector_type == "poco":
            elem = self.wait_for_element(selector)
            elem.click()
            logger.info(f"Poco点击: {selector}")
        elif selector_type == "image":
            touch(Template(selector))
            logger.info(f"图像点击: {selector}")

    def wait_for_element(self, poco_selector, timeout=None):
        timeout = timeout or self.wait_time
        elem = poco_selector.wait(timeout=timeout)
        if not elem.exists():
            raise TimeoutError(f"元素 {poco_selector} 在 {timeout}s 内未出现")
        return elem

    def get_text(self, poco_selector):
        elem = self.wait_for_element(poco_selector)
        text = elem.get_text()
        logger.info(f"获取文本: {text}")
        return text

    def input_text(self, poco_selector, text):
        elem = self.wait_for_element(poco_selector)
        elem.set_text(text)
        logger.info(f"输入: {text}")

    def clear_text(self, poco_selector):
        elem = self.wait_for_element(poco_selector)
        elem.set_text("")
        logger.info(f"清空文本框: {poco_selector}")

    def assert_exists(self, poco_selector, msg=None):
        try:
            self.wait_for_element(poco_selector, timeout=3)
            logger.info(f"断言存在成功: {poco_selector}")
            return True
        except TimeoutError:
            snapshot(msg=f"元素不存在_{msg}" if msg else "元素不存在")
            raise AssertionError(msg or f"元素 {poco_selector} 未出现")

    def take_screenshot(self,file_path=None, name="screenshot"):
        """
        截图并保存到指定目录
        :param file_path: 保存目录
        :param name: 文件名
        :return: 文件路径
        """
        # 默认保存目录
        if not file_path:
            file_path = SCREENSHOTS_DIR
        filename = file_path / f"{name}_{int(time.time())}.png"
        snapshot(filename=str(filename))
        logger.info(f"截图保存至: {filename}")
        return str(filename)

    def swipe(self, direction, duration=0.5):
        screen_width, screen_height = G.DEVICE.display_size
        if direction == "up":
            start = (screen_width // 2, screen_height * 3 // 4)
            end = (screen_width // 2, screen_height // 4)
        elif direction == "down":
            start = (screen_width // 2, screen_height // 4)
            end = (screen_width // 2, screen_height * 3 // 4)
        elif direction == "left":
            start = (screen_width * 3 // 4, screen_height // 2)
            end = (screen_width // 4, screen_height // 2)
        elif direction == "right":
            start = (screen_width // 4, screen_height // 2)
            end = (screen_width * 3 // 4, screen_height // 2)
        else:
            raise ValueError("direction must be up/down/left/right")
        swipe(start, end, duration=duration)
        logger.info(f"滑动: {direction}")

    def keyevent(self, key):
        keyevent(key)
        logger.info(f"按键: {key}")