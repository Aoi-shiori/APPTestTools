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


    @pytest.mark.skip(reason="调试用用例")
    @allure.feature("登录模块")          # 功能模块
    @allure.story("完整登录退出流程")     # 用户故事
    @allure.title("Case0:测试完整登录和退出流程")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    def test_full_login_and_logout(self):
        """完整登录-退出流程，包含隐私政策、条款验证"""


        # 1. 重置应用并启动
        with allure.step("重置应用并启动"):
            self.login_page.reset_app()

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
        self.login_page.select_site()

        # 7. 退出登录
        self.login_page.logout()

        # 8. 再次启动应用验证隐私政策内容（断言）
        self.login_page.launch_app()
        self.login_page.check_privacy()

        self.login_page.verify_privacy_policy()
        self.login_page.press_back()

        # 9. 验证条款与条件页面内容
        self.login_page.check_terms()
        self.login_page.verify_terms()
        self.login_page.press_back()

        # 10. 回到主页
        self.login_page.back_home()

    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case3:Tenant字段不输入或者输入为空，无法登录")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    @pytest.mark.parametrize("tenant,email,password", [("","jun@vivalink.com.cn", "Jun@1234"),(" ","jun@vivalink.com.cn", "Jun@1234")])
    def test_login_Case3(self,tenant,email,password):
        """Tenant字段不输入或者输入为空，无法登录"""

        # 1. 重置应用并启动
        with allure.step("重置应用并启动"):
            self.login_page.reset_app()

        # 2. 同意隐私政策与条款
        with allure.step("同意隐私政策与条款"):
            self.login_page.agree_privacy_and_terms()

        # 3. 输入账号信息
        with allure.step("输入账号信息"):
            self.login_page.input_credentials(
                tenant=tenant,
                email=email,
                password=password
            )

        # 4. 返回并登录
        with allure.step("返回并登录"):
            self.login_page.press_back()
            self.login_page.click_login()

        with allure.step("登录失败弹窗提示"):
            snapshot_path=self.login_page.check_login_failed_alert()
            if snapshot_path:
                allure.attach.file(
                    snapshot_path,
                    name="登录失败弹窗提示",
                    attachment_type=allure.attachment_type.PNG)





    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case4:输入已注册的Tenant，正常登录")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    def test_login_Case4(self):
        """输入已注册的Tenant，正常登录"""

        # 1. 重置应用并启动
        with allure.step("重置应用并启动"):
            self.login_page.reset_app()

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
            self.login_page.handle_notification_permission()
            self.login_page.select_site()


        # 7. 退出登录
        with allure.step("退出登录"):
            self.login_page.logout()



    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case5:输入已注册的Tenant 前后有空格，检查是否可以正常登录")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    @pytest.mark.parametrize("tenant,email,password", [(" first ","jun@vivalink.com.cn", "Jun@1234")])
    def test_login_Case5(self,tenant,email,password):

        # 1. 重置应用并启动
        with allure.step("重置应用并启动"):
            self.login_page.reset_app()

        # 2. 同意隐私政策与条款
        with allure.step("同意隐私政策与条款"):
            self.login_page.agree_privacy_and_terms()

        # 3. 输入账号信息
        with allure.step("输入账号信息，tenant前后有空格"):
            self.login_page.input_credentials(
                tenant=tenant,
                email=email,
                password=password
            )

        # 4. 返回并登录
        with allure.step("返回并登录"):
            self.login_page.press_back()
            self.login_page.click_login()
            self.login_page.handle_notification_permission()



        # 6. 选择站点（注意按钮包含换行符）
        with allure.step("选择站点"):
            self.login_page.select_site()
            self.login_page.handle_notification_permission()

        # 5. 登录页面截图
        with allure.step("打开个人侧面弹窗并截图"):
            snapshot_path = self.login_page.open_side_info()
            if snapshot_path:
                allure.attach.file(
                    snapshot_path,
                    name="登录成功个人信息页面截图",
                    attachment_type=allure.attachment_type.PNG
                )

        # 7. 退出登录
        with allure.step("退出登录"):
            self.login_page.logout()

    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case6:输入未注册的Tenant，登录失败")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    @pytest.mark.parametrize("tenant,email,password", [("first2026","jun@vivalink.com.cn", "Jun@1234")])
    def test_login_Case6(self,tenant,email,password):

        # 1. 重置应用并启动
        with allure.step("重置应用并启动"):
            self.login_page.reset_app()

        # 2. 同意隐私政策与条款
        with allure.step("同意隐私政策与条款"):
            self.login_page.agree_privacy_and_terms()

        # 3. 输入账号信息
        with allure.step("输入账号信息，tenant未注册"):
            self.login_page.input_credentials(
                tenant=tenant,
                email=email,
                password=password
            )

        # 4. 返回并登录
        with allure.step("返回并登录"):
            self.login_page.press_back()
            self.login_page.click_login()
            self.login_page.handle_notification_permission()



        with allure.step("登录失败弹窗提示"):
            snapshot_path=self.login_page.check_login_failed_alert()
            if snapshot_path:
                allure.attach.file(
                    snapshot_path,
                    name="登录失败弹窗提示",
                    attachment_type=allure.attachment_type.PNG)


    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case8:Email不输入或者输入为空，无法登录")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    @pytest.mark.parametrize("tenant,email,password", [("first","", "Jun@1234"),("first"," ", "Jun@1234")])
    def test_login_Case8(self,tenant,email,password):

        # 1. 重置应用并启动
        with allure.step("重置应用并启动"):
            self.login_page.reset_app()

        # 2. 同意隐私政策与条款
        with allure.step("同意隐私政策与条款"):
            self.login_page.agree_privacy_and_terms()

        # 3. 输入账号信息
        with allure.step("输入账号信息，Email不输入或者输入为空"):
            self.login_page.input_credentials(
                tenant=tenant,
                email=email,
                password=password
            )

        # 4. 返回并登录
        with allure.step("返回并登录"):
            self.login_page.press_back()
            self.login_page.click_login()
            self.login_page.handle_notification_permission()



        with allure.step("登录失败弹窗提示"):
            snapshot_path=self.login_page.check_login_failed_alert()
            if snapshot_path:
                allure.attach.file(
                    snapshot_path,
                    name="登录失败弹窗提示",
                    attachment_type=allure.attachment_type.PNG)


    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case9:Email格式不正确，无法登录")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    @pytest.mark.parametrize("tenant,email,password", [("first","jun@vivalink.com.cn1111", "Jun@1234")])
    def test_login_Case9(self,tenant,email,password):

        # 1. 重置应用并启动
        with allure.step("重置应用并启动"):
            self.login_page.reset_app()

        # 2. 同意隐私政策与条款
        with allure.step("同意隐私政策与条款"):
            self.login_page.agree_privacy_and_terms()

        # 3. 输入账号信息
        with allure.step("输入账号信息，Email格式不正确，无法登录"):
            self.login_page.input_credentials(
                tenant=tenant,
                email=email,
                password=password
            )

        # 4. 返回并登录
        with allure.step("返回并登录"):
            self.login_page.press_back()
            self.login_page.click_login()
            self.login_page.handle_notification_permission()



        with allure.step("登录失败弹窗提示"):
            snapshot_path=self.login_page.check_login_failed_alert()
            if snapshot_path:
                allure.attach.file(
                    snapshot_path,
                    name="登录失败弹窗提示",
                    attachment_type=allure.attachment_type.PNG)


    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case12:Email已注册且属于当前Tenant ，检查是否成功登录")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    def test_login_Case12(self):
        """Email已注册且属于当前Tenant ，检查是否成功登录"""
        # 1. 重置应用并启动
        with allure.step("重置应用并启动"):
            self.login_page.reset_app()

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
            self.login_page.handle_notification_permission()

        # 5. 处理条款弹窗（如果有）
        with allure.step("处理条款弹窗"):
            self.login_page.handle_terms_popup()

        # 6. 选择站点（注意按钮包含换行符）
        with allure.step("选择站点"):
            self.login_page.select_site()
            self.login_page.handle_notification_permission()


        # 7. 退出登录
        with allure.step("退出登录"):
            self.login_page.logout()

    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case15:密码正确，成功登录")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    def test_login_Case15(self):
        """密码正确，成功登录"""
        # 1. 重置应用并启动
        with allure.step("重置应用并启动"):
            self.login_page.reset_app()

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
            self.login_page.handle_notification_permission()
            self.login_page.select_site()

        # 7. 退出登录
        with allure.step("退出登录"):
            self.login_page.logout()

    @allure.feature("登录模块")          # 功能模块
    @allure.story("REQ 1.14")     # 用户故事
    @allure.title("Case21:检查勾选Privacy Policy/Terms &Conditions后，是否登录成功")  # 用例标题
    @allure.severity(allure.severity_level.CRITICAL)  # 标记严重程度
    def test_login_Case21(self):
        """检查勾选Privacy Policy/Terms &Conditions后，是否登录成功"""
        # 1. 重置应用并启动
        with allure.step("重置应用并启动"):
            self.login_page.reset_app()

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
            self.login_page.handle_notification_permission()

        # 5. 处理条款弹窗（如果有）
        with allure.step("处理条款弹窗"):
            self.login_page.handle_terms_popup()

        # 6. 选择站点（注意按钮包含换行符）
        with allure.step("选择站点"):
            self.login_page.select_site()
            self.login_page.handle_notification_permission()

        # 7. 退出登录
        with allure.step("退出登录"):
            self.login_page.logout()

    @allure.feature("登录模块")
    @allure.story("REQ 1.14")
    @allure.title("Case22:检查Privacy Policy/Terms &Conditions链接跳转的页面")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_Case22(self):
        with allure.step("重置应用并启动"):
            self.login_page.reset_app()

        with allure.step("验证隐私政策内容"):
            snapshot_path = self.login_page.verify_privacy_policy()
            logger.info("隐私政策内容验证成功.")
            # 截图并附加到allure
            if snapshot_path:
                allure.attach.file(snapshot_path, name="隐私政策页面", attachment_type=allure.attachment_type.PNG)

        with allure.step("关闭弹窗键盘"):
            if self.login_page.is_keyboard_visible():
                self.login_page.press_back()

        with allure.step("验证条款与条件页面"):
            snapshot_path = self.login_page.verify_terms()
            # snapshot 返回截图路径
            if snapshot_path:
                allure.attach.file(snapshot_path, name="条款验证结果截图", attachment_type=allure.attachment_type.PNG)

        with allure.step("回到主页"):
            self.login_page.back_home()