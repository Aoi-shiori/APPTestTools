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
from airtest.core.api import sleep, keyevent, assert_exists, snapshot
from utils.image_helper import get_template
import allure
import time
from utils.logger import get_logger


logger = get_logger(__name__)

class LoginPage(BasePage):
    """登录相关页面对象"""

    # ========== 元素定位常量 ==========
    APP_NAME = "Multi Vital Monitor"

    #个人信息图标
    BTN_USER_INFO = "JU"
    # 登录按钮
    BTN_LOGIN = "Login"
    #退出登录按钮
    BTN_LOGOUT = "Logout"
    BTN_ABOUT="About"
    BTN_LEGAL="Legal"
    BTN_SUPPORT="Support"

    BTN_OK = "OK"
    BTN_CANCEL = "Cancel"
    BTN_ACCEPT = "Accept"

    # 通知权限弹窗
    MESSAGE_NOTIFICATION_PERMISSION = "android.widget.ScrollView"
    BTN_NOTIFICATION_PERMISSION_DENY="com.android.permissioncontroller:id/permission_deny_button"
    BTN_NOTIFICATION_PERMISSION_ALLOW="com.android.permissioncontroller:id/permission_allow_button"


    # 确认信息弹窗
    MESSAGE_DIALOG_LOCKDOWN_MODE_TITLE = "Lockdown Mode Active"
    MESSAGE_DIALOG_TERMS_AND_CONDITIONS_REQUIRED_TITLE = "Terms & Conditions Required"
    MESSAGE_DIALOG_SITE_SELECT_TITLE="Please select site"




    # 隐私政策页面验证模板
    PRIVACY_POLICY_LINK="Privacy Policy"
    PRIVACY_POLICY_TEMPLATE = r"privacy_policy.png"
    PRIVACY_POLICY_RECORD_POS = (-0.004, 0.027)
    PRIVACY_POLICY_RESOLUTION = (1080, 2400)

    # 条款与条件页面验证模板
    TERMS_TEMPLATE_LINK="Terms & Conditions"
    TERMS_TEMPLATE = r"Terms_Conditions.png"
    TERMS_RECORD_POS = (-0.005, 0.028)
    # TERMS_TEMPLATE = r"tpl1776849861954.png"
    # TERMS_RECORD_POS = (-0.005, 0.014)
    TERMS_RESOLUTION = (1080, 2400)


    # 登录页面验证模板
    LOGIN_TEMPLATE = r"login_UI.png"
    LOGIN_RECORD_POS = (-0.001, 0.018)
    LOGIN_RESOLUTION = (1080, 2400)

    # 测试数据（可根据需要移至配置文件，此处仅为示例）
    TEST_TENANT = "first"
    TEST_EMAIL = "jun@vivalink.com.cn"
    TEST_PASSWORD = "Jun@1234"
    SITE_BUTTON_TEXT = "first\nRegistered"
    LOGOUT_INITIALS = "VI"

    # ===================================================

    # 启动应用
    def launch_app(self, app_name=APP_NAME):
        keyevent(self.BTN_HOME)
        self.poco(text=app_name).click()
        sleep(2)

    # 同意隐私政策和条款
    def agree_privacy_and_terms(self):
        is_checked = self.poco("android.widget.CheckBox").attr('checked')
        if is_checked:
            return
        else:
            self.poco("android.widget.CheckBox").click()

    # 验证隐私政策页面（封装断言和截图）
    def verify_privacy_policy(self):
        """点击隐私政策链接，验证页面内容并截图"""
        self.poco(self.PRIVACY_POLICY_LINK).click()
        sleep(1)
        # 使用类常量进行验证
        assert_exists(
            get_template(
                self.PRIVACY_POLICY_TEMPLATE,
                record_pos=self.PRIVACY_POLICY_RECORD_POS,
                resolution=self.PRIVACY_POLICY_RESOLUTION
            ),
            "隐私政策内容存在"
        )
        snapshot_path = self.take_screenshot(name="隐私政策页面结果")
        # 返回按钮点击
        self.press_back()
        return snapshot_path

    # 验证条款与条件页面
    def verify_terms(self):
        """点击条款与条件链接，验证页面内容并截图"""
        self.poco(self.TERMS_TEMPLATE_LINK).click()
        sleep(1)
        assert_exists(
            get_template(
                self.TERMS_TEMPLATE,
                record_pos=self.TERMS_RECORD_POS,
                resolution=self.TERMS_RESOLUTION
            ),
            "条款与条件页存在"
        )
        snapshot_path=self.take_screenshot(name="条款与条件页面结果")
        self.press_back()
        return snapshot_path

    # 验证登录页面 UI
    def verify_login_ui(self):
        """验证登录页面 UI """
        sleep(1)
        # 使用类常量进行验证
        assert_exists(
            get_template(
                self.LOGIN_TEMPLATE,
                record_pos=self.LOGIN_RECORD_POS,
                resolution=self.LOGIN_RESOLUTION
            ),
            "UI页面符合原型"
        )
        snapshot_path = self.take_screenshot(name="登录UI页面验证结果")
        # 返回按钮点击
        self.press_back()
        return snapshot_path


    # 为了向后兼容，保留原有的 check_privacy / check_terms（仅点击，不做断言）
    def check_privacy(self):
        self.poco(self.PRIVACY_POLICY_LINK).click()
        sleep(1)

    def check_terms(self):
        self.poco(self.TERMS_TEMPLATE_LINK).click()
        sleep(1)

    # 输入租户、邮箱、密码
    def input_credentials(self, tenant, email, password):
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

    # 点击登录按钮
    def click_login(self):
        self.poco(self.BTN_LOGIN).click()
        sleep(3)

    # 处理“需要同意条款与条件”弹窗
    def handle_terms_popup(self):
        if self.poco(self.MESSAGE_DIALOG_TERMS_AND_CONDITIONS_REQUIRED_TITLE).exists():
            self.poco(self.BTN_ACCEPT).click()

    # 选择站点（按钮文本可能包含换行符）
    def select_site(self, site_name=None):
        if site_name is None:
            site_name = self.SITE_BUTTON_TEXT   # 使用默认常量
        if self.poco(self.MESSAGE_DIALOG_SITE_SELECT_TITLE).wait(timeout=10):
            try:
                snapshot_path=self.take_screenshot(name="站点列表弹窗")
                self.poco(name=site_name).click()

                if snapshot_path:
                    return snapshot_path
                else:
                    return False
            except:
                try:
                    self.poco(text=site_name).click()
                except:
                    try:
                        self.poco(desc=site_name).click()
                    except:
                        self.poco("android.widget.Button").wait(timeout=3)[0].click()

        else:
            raise Exception("未出现站点选择弹窗")

    # 退出登录（根据用户首字母）
    def logout(self, user_indicator=None):
        if user_indicator is None:
            user_indicator = self.LOGOUT_INITIALS
        if self.poco(user_indicator).exists():
            self.poco(user_indicator).click()
            self.poco(self.BTN_LOGOUT).click()
            if self.poco(self.MESSAGE_DIALOG_LOCKDOWN_MODE_TITLE).wait(timeout=3).exists():
                self.poco(self.BTN_OK).click()
                self.keyevent(self.BTN_BACK)
                self.poco("android.widget.Button").click()
                self.poco("android.widget.EditText").set_text(self.TEST_PASSWORD)
                self.poco(self.BTN_OK).click()
                self.poco(self.BTN_USER_INFO).wait(timeout=2).click()
                self.poco(self.BTN_LOGOUT).click()
            else:
                self.keyevent(self.BTN_HOME)
        else:
            if self.poco(self.BTN_USER_INFO).wait(timeout=3).exists():
                self.poco(self.BTN_USER_INFO).click()
                self.poco(self.BTN_LOGOUT).click()
            self.back_home()

    # 处理通知权限弹窗
    def handle_notification_permission(self):
        """
        处理通知权限弹窗，循环检测直到弹窗消失或超时
        :return: 是否成功处理了弹窗
        """
        timeout = 15  # 最多等待10秒
        start_time = time.time()
        handled = False

        while time.time() - start_time < timeout:
            try:
                # 每次循环重新获取控件，避免引用失效
                allow_btn = self.poco(self.BTN_NOTIFICATION_PERMISSION_ALLOW)
                if allow_btn.exists():
                    allow_btn.click()
                    handled = True
                    logger.info("已点击允许通知权限")
                    # 点击后等待弹窗关闭
                    sleep(0.5)
                    continue
            except Exception as e:
                logger.warning(f"检查权限弹窗时出错: {e}")

            # 检查弹窗是否已经消失（没有允许按钮，也没有拒绝按钮）
            try:
                if not self.poco(self.MESSAGE_NOTIFICATION_PERMISSION).exists():
                    logger.info("通知权限弹窗已消失")
                    sleep(1)
                    break
            except:
                pass
        else:
            logger.warning("处理通知权限弹窗超时，未检测到弹窗或无法处理")

        return handled

    # 期望 site 列表处理
    def handle_expected_site_list(self, expected_sites=None):
        """
        确保站点列表仅包含期望的站点。
        若未传入 expected_sites，则使用默认列表 ["first", "first2", "first3"]。

        """
        default_sites_list=["first", "first2", "first3"]


        if expected_sites is None:
            expected_sites = ["first", "first2", "first3"]
        else:
            expected_sites = set(expected_sites).union(set(default_sites_list))
        logger.info("expected_sites: %s" % expected_sites)

        # 1. 删除所有不属于期望列表的站点
        sites = self.settings_api.get_sites()
        sites_list = [site["name"] for site in sites]
        for site in sites:
            if site["name"] not in expected_sites:
                self.settings_api.delete_site(site["name"])
                logger.info(f"删除站点：{site['name']}")

        # 2. 添加缺失的期望站点
        current_sites = self.settings_api.get_sites()
        current_names = [site["name"] for site in current_sites]
        for expected in expected_sites:
            if expected not in current_names:
                self.settings_api.add_site(expected)
                logger.info("添加缺失的期望站点：%s" % expected)
        return sites_list

    def check_login_failed_alert(self):
       if self.wait_for_element(self.poco("Error")):
           if self.poco("[400] invalid Name: value length must be between 1 and 100 runes, inclusive").exists():
                logger.info("登录失败,invalid Name: value length must be between 1 and 100 runes")
                snapshot_path = self.take_screenshot(name="400_invalid_Name登录失败页面结果")
                self.tap_element(self.poco("OK"))
                return snapshot_path
           elif self.poco("[404] Tenant not found.").exists():
                 logger.info("登录失败,[404] Tenant not found.")
                 snapshot_path = self.take_screenshot(name="404_Tenant_not_found登录失败页面结果")
                 self.tap_element(self.poco("OK"))
                 return snapshot_path
           elif self.poco("[400] Incorrect email or password. Try again or reset your password.").exists():
                logger.info("登录失败,Invalid argument(s): The email format is incorrect.")
                snapshot_path = self.take_screenshot(name="400_Incorrect_email_or_password登录失败页面结果")
                self.tap_element(self.poco("OK"))
                return snapshot_path
           elif self.poco("Invalid argument(s): The email format is incorrect.").exists():
                logger.info("登录失败,Invalid argument(s): The email format is incorrect.")
                snapshot_path = self.take_screenshot(name="The_email_format_is_incorrect登录失败页面结果")
                self.tap_element(self.poco("OK"))
                return snapshot_path
           else:
             return  False
       else:
           return False