#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/15 14:16
@File: test_login.py
@IDE: PyCharm
@Description: 
"""
import pytest
from airtest.core.api import *

from pages.login_page import LoginPage
from utils.image_helper import get_template
from utils.logger import get_logger
import allure


logger = get_logger("TestLogin")


class TestLogin:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.login_page = LoginPage()
        auto_setup(__file__)
        self.login_page.back_home()


    @pytest.mark.skip(reason="调试用用例")
    @allure.feature("登录模块")          # 功能模块
    @allure.story("完整登录退出流程")     # 用户故事
    @allure.title("Case0:测试完整登录和退出流程")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    def test_full_login_and_logout(self):
        """完整登录-退出流程，包含隐私政策、条款验证"""


        # 1. 启动应用
        self.login_page.launch_app("Multi Vital Monitor")

        # 2. 同意隐私政策与条款
        self.login_page.agree_privacy_and_terms()

        # 3. 输入账号信息
        self.login_page.input_credentials(
            tenant="first",
            email="jun@vivalink.com.cn",
            password="Jun@1234"
        )

        # 4. 返回并登录
        self.login_page.press_back()
        self.login_page.click_login()

        # 5. 处理条款弹窗（如果有）
        self.login_page.handle_terms_popup()

        # 6. 选择站点（注意按钮包含换行符）
        self.login_page.select_site("first\nRegistered")

        # 7. 退出登录
        self.login_page.logout("VI")

        # 8. 再次启动应用验证隐私政策内容（断言）
        self.login_page.launch_app()
        self.login_page.check_privacy()

        assert_exists(get_template(r"tpl1776239168968.png", record_pos=(0.008, -0.024), resolution=(1080, 2400)),
                      "隐私政策内容存在")
        logger.info("隐私政策内容验证成功.")
        snapshot(msg="隐私验证结果截图.")
        self.login_page.poco("返回").click()

        # 9. 验证条款与条件页面内容
        self.login_page.check_terms()
        # self.login_page.poco("条款与条件").click()
        assert_exists(get_template(r"tpl1776232511072.png", record_pos=(0.017, -0.36), resolution=(1080, 2400)),
                      "条款与条件页存在")
        snapshot(msg="条款验证结果截图.")
        self.login_page.poco("返回").click()

        # 10. 回到主页
        keyevent("HOME")

    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case4:输入已注册的Tenant，正常登录")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    def test_login_Case4(self):
        """输入已注册的Tenant，正常登录"""

        # 1. 启动应用
        with allure.step("启动应用"):
            self.login_page.launch_app("Multi Vital Monitor")

        # 2. 同意隐私政策与条款
        with allure.step("同意隐私政策与条款"):
            self.login_page.agree_privacy_and_terms()

        # 3. 输入账号信息
        with allure.step("输入账号信息"):
            self.login_page.input_credentials(
                tenant="first",
                email="jun@vivalink.com.cn",
                password="Jun@1234"
            )

        # 4. 返回并登录
        with allure.step("返回并登录"):
            self.login_page.press_back()
            self.login_page.click_login()

        # 5. 处理条款弹窗（如果有）
        with allure.step("处理条款弹窗"):
            self.login_page.handle_terms_popup()

        # 6. 选择站点（注意按钮包含换行符）
        with allure.step("选择站点"):
            self.login_page.select_site("first\nRegistered")

        # 7. 退出登录
        with allure.step("退出登录"):
            self.login_page.logout("VI")

    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case12:Email已注册且属于当前Tenant ，检查是否成功登录")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    def test_login_Case12(self):
        """Email已注册且属于当前Tenant ，检查是否成功登录"""
        # 1. 启动应用
        with allure.step("启动应用"):
            self.login_page.launch_app("Multi Vital Monitor")

        # 2. 同意隐私政策与条款
        with allure.step("同意隐私政策与条款"):
            self.login_page.agree_privacy_and_terms()

        # 3. 输入账号信息
        with allure.step("输入账号信息"):
            self.login_page.input_credentials(
                tenant="first",
                email="jun@vivalink.com.cn",
                password="Jun@1234"
            )

        # 4. 返回并登录
        with allure.step("返回并登录"):
            self.login_page.press_back()
            self.login_page.click_login()

        # 5. 处理条款弹窗（如果有）
        with allure.step("处理条款弹窗"):
            self.login_page.handle_terms_popup()

        # 6. 选择站点（注意按钮包含换行符）
        with allure.step("选择站点"):
            self.login_page.select_site("first\nRegistered")

        # 7. 退出登录
        with allure.step("退出登录"):
            self.login_page.logout("VI")

    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case15:密码正确，成功登录")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    def test_login_Case15(self):
        """密码正确，成功登录"""

        # 1. 启动应用
        with allure.step("启动应用"):
            self.login_page.launch_app("Multi Vital Monitor")

        # 2. 同意隐私政策与条款
        with allure.step("同意隐私政策与条款"):
            self.login_page.agree_privacy_and_terms()

        # 3. 输入账号信息
        with allure.step("输入账号信息"):
            self.login_page.input_credentials(
                tenant="first",
                email="jun@vivalink.com.cn",
                password="Jun@1234"
            )

        # 4. 返回并登录
        with allure.step("返回并登录"):
            self.login_page.press_back()
            self.login_page.click_login()

        # 5. 处理条款弹窗（如果有）
        with allure.step("处理条款弹窗"):
            self.login_page.handle_terms_popup()

        # 6. 选择站点（注意按钮包含换行符）
        with allure.step("选择站点"):
            self.login_page.select_site("first\nRegistered")

        # 7. 退出登录
        with allure.step("退出登录"):
            self.login_page.logout("VI")

    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case21:检查勾选Privacy Policy/Terms &Conditions后，是否登录成功")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    def test_login_Case21(self):
        """检查勾选Privacy Policy/Terms &Conditions后，是否登录成功"""

        # 1. 启动应用
        with allure.step("启动应用"):
            self.login_page.launch_app("Multi Vital Monitor")

        # 2. 同意隐私政策与条款
        with allure.step("同意隐私政策与条款"):
            self.login_page.agree_privacy_and_terms()

        # 3. 输入账号信息
        with allure.step("输入账号信息"):
            self.login_page.input_credentials(
                tenant="first",
                email="jun@vivalink.com.cn",
                password="Jun@1234"
            )

        # 4. 返回并登录
        with allure.step("返回并登录"):
            self.login_page.press_back()
            self.login_page.click_login()

        # 5. 处理条款弹窗（如果有）
        with allure.step("处理条款弹窗"):
            self.login_page.handle_terms_popup()

        # 6. 选择站点（注意按钮包含换行符）
        with allure.step("选择站点"):
            self.login_page.select_site("first\nRegistered")

        # 7. 退出登录
        with allure.step("退出登录"):
            self.login_page.logout("VI")


    @allure.feature("登录模块")
    @allure.story("REQ 1.14")
    @allure.title("Case22:检查Privacy Policy/Terms &Conditions链接跳转的页面")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_Case22(self):
        """检查Privacy Policy/Terms &Conditions链接跳转的页面"""
        with allure.step("启动应用"):
            self.login_page.launch_app("Multi Vital Monitor")

        with allure.step("验证隐私政策内容"):
            self.login_page.check_privacy()
            assert_exists(get_template(r"tpl1776239168968.png", record_pos=(0.008, -0.024), resolution=(1080, 2400)),
                          "隐私政策内容存在")
            logger.info("隐私政策内容验证成功.")
            # 截图并附加到allure
            img_path = self.login_page.take_screenshot(name="隐私政策页面结果")  # 假设返回路径
            if img_path:
                allure.attach.file(img_path, name="隐私政策页面", attachment_type=allure.attachment_type.PNG)
            self.login_page.poco("返回").click()

        with allure.step("验证条款与条件页面"):
            self.login_page.check_terms()
            assert_exists(get_template(r"tpl1776232511072.png", record_pos=(0.017, -0.36), resolution=(1080, 2400)),
                          "条款与条件页存在")
            # snapshot 返回截图路径
            snapshot_path = self.login_page.take_screenshot(name="条款验证结果截图结果")
            if snapshot_path:
                allure.attach.file(snapshot_path, name="条款验证结果截图", attachment_type=allure.attachment_type.PNG)
            self.login_page.poco("返回").click()

        with allure.step("退出登录"):
            self.login_page.logout("VI")

        with allure.step("回到主页"):
            keyevent("HOME")

    #TODO 待完善
    @pytest.mark.skip(reason="待完善，跳过此用例")
    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case24:Tenant 下已添加多个 Site，登录时检查 Site 筛选窗")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    def test_login_Case24(self):
        """Tenant 下已添加多个 Site，登录时检查 Site 筛选窗"""

        # 1. 启动应用
        with allure.step("启动应用"):
            self.login_page.launch_app("Multi Vital Monitor")

        # 2. 同意隐私政策与条款
        with allure.step("同意隐私政策与条款"):
            self.login_page.agree_privacy_and_terms()

        # 3. 输入账号信息
        with allure.step("输入账号信息"):
            self.login_page.input_credentials(
                tenant="first",
                email="jun@vivalink.com.cn",
                password="Jun@1234"
            )

        # 4. 返回并登录
        with allure.step("返回并登录"):
            self.login_page.press_back()
            self.login_page.click_login()

        # 5. 处理条款弹窗（如果有）
        with allure.step("处理条款弹窗"):
            self.login_page.handle_terms_popup()

        # 6. 选择站点（注意按钮包含换行符）
        with allure.step("选择站点"):
            self.login_page.select_site("first\nRegistered")

        # 7. 退出登录
        with allure.step("退出登录"):
            self.login_page.logout("VI")


    # TODO: 待完善
    @pytest.mark.skip(reason="未完成用例跳过")
    @allure.feature("登录模块")  # 功能模块
    @allure.story("REQ 1.14")  # 用户故事
    @allure.title("Case24:Tenant admin登录Standard user 账号是否弹出site筛选窗")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    def test_login_Case27(self):
        """Tenant admin登录Standard user 账号是否弹出site筛选窗"""

        # 1. 启动应用
        with allure.step("启动应用"):
            self.login_page.launch_app("Multi Vital Monitor")

        # 2. 同意隐私政策与条款
        with allure.step("同意隐私政策与条款"):
            self.login_page.agree_privacy_and_terms()

        # 3. 输入账号信息
        with allure.step("输入账号信息"):
            self.login_page.input_credentials(
                tenant="first",
                email="jun@vivalink.com.cn",
                password="Jun@1234"
            )

        # 4. 返回并登录
        with allure.step("返回并登录"):
            self.login_page.press_back()
            self.login_page.click_login()

        # 5. 处理条款弹窗（如果有）
        with allure.step("处理条款弹窗"):
            self.login_page.handle_terms_popup()

        # 6. 选择站点（注意按钮包含换行符）
        with allure.step("选择站点"):
            self.login_page.select_site("first2")

        # 7. 退出登录
        with allure.step("退出登录"):
            self.login_page.logout("VI")