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
from airtest.core.api import G,touch, swipe, exists, Template, snapshot, keyevent,start_app, stop_app, clear_app, sleep, device
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from config.settings import WAIT_TIME, SCREENSHOTS_DIR
from utils.logger import get_logger
import time
import subprocess
from api.settings_api import SettingsAPI

logger = get_logger()


class BasePage:
    """基础页面"""
    #主页按钮
    BTN_HOME = "HOME"
    #返回按钮
    BTN_BACK = "BACK"

    # 个人信息图标坐标
    """
        x = 0.087037 * width
        y = 0.087083 * height
    """
    USER_ICON_COORDINATES=(0.087037,0.087083)

    def __init__(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        self.wait_time = WAIT_TIME
        self.device = device()
        self.settings_api=SettingsAPI()


    def tap_element(self, selector, selector_type="poco"):
        """
            点击元素
            :param element
            :return None
        """
        if selector_type == "poco":
            elem = self.wait_for_element(selector)
            elem.click()
            logger.info(f"Poco点击: {selector}")
        elif selector_type == "image":
            touch(Template(selector))
            logger.info(f"图像点击: {selector}")

    def wait_for_element(self, poco_selector, timeout=None):
        """
        等待元素出现
        :param poco_selector: poco选择器
        :param timeout: 超时时间
        :return:
        """
        # poco_selector = self.poco(poco_selector)
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

    # 返回主页
    def back_home(self):
        self.keyevent(self.BTN_HOME)
    # 返回键
    def press_back(self):
        self.keyevent(self.BTN_BACK)
        sleep(1)

    def reset_app(self, package_name="com.vivalink.vcloud2"):
        """
        重置应用
        :param package_name: 默认com.vivalink.vcloud2
        :return:
        """
        # 1. 终止应用进程
        stop_app(package_name)
        sleep(2)

        # 2. 清除应用数据
        clear_app(package_name)
        sleep(1)
        logger.info("已清除应用数据：%s" % package_name)

        # 3. 重新启动应用
        start_app(package_name)
        logger.info("正在启动应用：%s" % package_name)

        # 4. 使用 ADB 直接检测前台包名（不依赖 Airtest 内部方法）
        def get_foreground_package():
            try:
                # adb shell dumpsys window | grep mCurrentFocus
                result = subprocess.run(
                    ["adb", "shell", "dumpsys", "window", "|", "grep", "mCurrentFocus"],
                    capture_output=True, text=True, timeout=5
                )
                output = result.stdout.strip()
                # 输出格式：mCurrentFocus=Window{xxx u0 com.example.app/com.example.MainActivity}
                import re
                match = re.search(r'u0\s+([\w\.]+)/', output)
                if match:
                    return match.group(1)
            except Exception as e:
                logger.warning(f"获取前台包名失败: {e}")
            return None

        # 等待最多 15 秒，直到前台包名匹配
        for i in range(15):
            sleep(1)
            current_pkg = get_foreground_package()
            if current_pkg == package_name:
                logger.info(f"应用已成功启动：{package_name}")
                break
        else:
            logger.error(f"应用启动超时，未检测到前台包名：{package_name}")
        sleep(3)  # 额外等待界面稳定，根据机型配置选择

    def is_keyboard_visible(self):
        """判断键盘是否可见（支持 Google 输入法）"""
        # 可根据需要添加更多输入法的标识
        keyboard_indicators = [
            "com.google.android.inputmethod.latin:id/keyboard_holder",
            "com.android.inputmethod.keyboard",   # 其他输入法的通用标识
            "android.inputmethodservice.KeyboardView"
        ]
        for indicator in keyboard_indicators:
            try:
                if self.poco(indicator).exists():
                    # 可选：进一步检查可见性属性
                    return True
            except:
                continue
        return False

    # 获取 device
    def get_device(self):
        return self.device

    # 打开侧面信息窗口
    def open_side_info(self):
        width, height = self.get_device().get_current_resolution()
        self.USER_ICON_COORDINATES = [self.USER_ICON_COORDINATES[0] * width, self.USER_ICON_COORDINATES[1] * height]
        touch(self.USER_ICON_COORDINATES)
        snapshot_path = self.take_screenshot(name="个人信息侧窗页面截图")
        if snapshot_path:
            return snapshot_path
        return False

    def get_settings_api(self):
        return self.settings_api


