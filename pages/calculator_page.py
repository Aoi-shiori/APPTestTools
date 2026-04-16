#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/13 17:31
@File: calculator_page.py
@IDE: PyCharm
@Description: 
"""
from core.base_page import BasePage
from airtest.core.api import sleep

class CalculatorPage(BasePage):
    """Google 计算器页面对象（根据实际包名和控件ID调整）"""

    # 控件定位器（使用 Poco 选择器）
    DIGIT_1 = lambda self: self.poco("com.google.android.calculator:id/digit_1")
    DIGIT_2 = lambda self: self.poco("com.google.android.calculator:id/digit_2")
    DIGIT_3 = lambda self: self.poco("com.google.android.calculator:id/digit_3")
    DIGIT_4 = lambda self: self.poco("com.google.android.calculator:id/digit_4")
    DIGIT_5 = lambda self: self.poco("com.google.android.calculator:id/digit_5")
    DIGIT_6 = lambda self: self.poco("com.google.android.calculator:id/digit_6")
    DIGIT_7 = lambda self: self.poco("com.google.android.calculator:id/digit_7")
    DIGIT_8 = lambda self: self.poco("com.google.android.calculator:id/digit_8")
    DIGIT_9 = lambda self: self.poco("com.google.android.calculator:id/digit_9")
    DIGIT_0 = lambda self: self.poco("com.google.android.calculator:id/digit_0")
    OP_ADD = lambda self: self.poco("com.google.android.calculator:id/op_add")
    OP_SUB = lambda self: self.poco("com.google.android.calculator:id/op_sub")
    OP_MUL = lambda self: self.poco("com.google.android.calculator:id/op_mul")
    OP_DIV = lambda self: self.poco("com.google.android.calculator:id/op_div")
    OP_EQ = lambda self: self.poco("com.google.android.calculator:id/eq")
    BTN_CLEAR = lambda self: self.poco("com.google.android.calculator:id/clr")

    RESULT_FIELD = lambda self: self.poco("com.google.android.calculator:id/result_final")

    def click_digit(self, number):
        """点击数字（0-9）"""
        mapper = {
            '0': self.DIGIT_0, '1': self.DIGIT_1, '2': self.DIGIT_2,
            '3': self.DIGIT_3, '4': self.DIGIT_4, '5': self.DIGIT_5,
            '6': self.DIGIT_6, '7': self.DIGIT_7, '8': self.DIGIT_8,
            '9': self.DIGIT_9,
        }
        for digit in str(number):
            mapper[digit]().click()
            sleep(0.2)

    def add(self, a, b):
        """加法运算"""
        self.click_digit(a)
        self.OP_ADD().click()
        self.click_digit(b)
        self.OP_EQ().click()

    def get_result(self):
        """获取计算结果文本"""
        return self.get_text(self.RESULT_FIELD())

    def clear(self):
        """清空"""
        self.BTN_CLEAR().click()

    def ele_exists(self, selector):
        """判断元素是否存在"""
        return self.poco(selector).exists()