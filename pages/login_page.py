#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/15 10:09
@File: login_page.py
@IDE: PyCharm
@Description: 
"""
from core.base_page import BasePage
from airtest.core.api import sleep, keyevent

class LoginPage(BasePage):
    """登录相关页面对象"""

    # 启动应用
    def launch_app(self, app_name="Multi Vital Monitor"):
        keyevent("HOME")
        self.poco(text=app_name).click()
        sleep(2)

    # 同意隐私政策和条款
    def agree_privacy_and_terms(self):
        is_checked=self.poco("android.widget.CheckBox").attr('checked')
        if is_checked:
            return
        else:
            self.poco("android.widget.CheckBox").click()

    # 验证隐私政策页面
    def check_privacy(self):
        self.poco("隐私政策").click()
        sleep(1)
    # 检查条款
    def check_terms(self):
         self.poco("条款与条件").click()
         sleep(1)

    # 输入租户、邮箱、密码
    def input_credentials(self, tenant, email, password):
        # self.poco("android.widget.EditText").wait_for_appearance(timeout=5)
        all_inputs = self.poco("android.widget.EditText")
        if len(all_inputs) >= 3:
            tenant_input = all_inputs[0]
            email_input = all_inputs[1]
            pwd_input = all_inputs[2]

            self.clear_text(tenant_input)
            tenant_input.click()
            self.input_text(tenant_input, tenant)

            self.clear_text(email_input)
            email_input.click()
            self.input_text(email_input, email)

            self.clear_text(pwd_input)
            pwd_input.click()
            self.input_text(pwd_input, password)
        else:
            raise Exception(f"只找到 {len(all_inputs)} 个输入框，预期至少3个")

    #返回键
    def press_back(self):
        self.keyevent("BACK")

    # 点击登录按钮
    def click_login(self):
        self.poco("登录").click()

    # 处理“需要同意条款与条件”弹窗
    def handle_terms_popup(self):
        if self.poco("需要同意条款与条件").exists():
            self.poco("同意").click()

    # 选择站点（按钮文本可能包含换行符）
    def select_site(self, site_name="first\nRegistered"):
        if self.poco("请选择站点").wait(timeout=5):
            # 尝试多种属性定位
            try:
                self.poco(name=site_name).click()
            except:
                try:
                    self.poco(text=site_name).click()
                except:
                    try:
                        self.poco(desc=site_name).click()
                    except:
                        # 最后尝试点击任意第一个按钮
                        self.poco("android.widget.Button").wait(timeout=3)[0].click()
        else:
            raise Exception("未出现站点选择弹窗")

    # 退出登录（根据用户首字母）
    def logout(self, user_indicator="VI"):
        if self.poco(user_indicator).exists():
            self.poco(user_indicator).click()
            self.poco("退出登录").click()
            # 处理锁定模式弹窗
            if self.poco("锁定模式已激活").wait(timeout=3).exists():
                self.poco("确定").click()
                self.keyevent("BACK")
                self.poco("android.widget.Button").click()
                self.poco("android.widget.EditText").set_text("Jun@1234")
                self.poco("确认").click()
                self.poco("Ju").wait(timeout=2).click()
                self.poco("退出登录").click()
            else:
                self.keyevent("HOME")
        else:
            # 尝试其他用户标识
            if self.poco("JU").wait(timeout=3).exists():
                self.poco("JU").click()
                self.poco("退出登录").click()
        self.keyevent("HOME")

    # 返回主页
    def back_home(self):
        self.keyevent("HOME")