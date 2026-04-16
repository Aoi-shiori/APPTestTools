#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/13 17:33
@File: test_calculator.py
@IDE: PyCharm
@Description: 
"""

import pytest
from pages.calculator_page import CalculatorPage

class TestCalculator:
    """计算器功能测试（弱手主要编写区域）"""
    # 跳过执行
    @pytest.mark.skip
    def test_addition(self, base_page):
        """测试 1+1=2"""
        calc = CalculatorPage()
        calc.add(1, 1)
        result = calc.get_result()
        assert result == "2", f"期望2，实际{result}"
    @pytest.mark.skip
    def test_clear(self, base_page):
        """测试清空功能"""
        calc = CalculatorPage()
        calc.add(5, 3)
        calc.clear()
        # 清空后，结果区域应该为空或显示0（根据实际应用调整）
        result = calc.RESULT_FIELD().exists()
        # 判断是否存在元素
        assert result, "清空后结果区域为空"
        # assert result == "0" or result == "" or result==None, f"清空后结果应为0，实际{result}"
