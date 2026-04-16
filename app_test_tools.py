#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/13 15:52
@File: app_test_tools.py
@IDE: PyCharm
@Description: 
"""
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# 1. 初始化 Poco 实例，用于控件定位
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 2. 初始化环境，自动连接设备（连接方法见下一步）
# 连接默认的Android设备
auto_setup(__file__, devices=["Android:///"])

# 连接指定设备，格式为 Android://ADB服务地址:端口/设备序列号
auto_setup(__file__, devices=["Android://127.0.0.1:5037/27261FDH2004A2"])

# # 连接夜神模拟器（端口62001）
# auto_setup(__file__, devices=["Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP"])
#
# # 连接雷电模拟器（端口5555）
# auto_setup(__file__, devices=["Android://127.0.0.1:5037/127.0.0.1:5555"])

# 使用 poco 进行控件定位（更稳定）
# 点击文本为“计算器”的应用图标
poco(text="计算器").click()
for node in poco.dump():
    print(node)

#例如，先定位到计算器的数字键盘区域（需根据实际情况调整）
keypad = poco("com.example.calculator:id/keypad")
keypad.child(text="1").click()


# 在计算器应用中执行加法操作
# elem = poco(text="1").wait(timeout=3)
# elem=poco(textMatches=".*1.*")
# elem.click()
poco(text="+").click()
poco(text="1").click()
poco(text="=").click()

if __name__ == '__main__':
    pass