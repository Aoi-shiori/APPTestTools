#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/23 17:00
@File: auth_api.py
@IDE: PyCharm
@Description: 
"""
from core.api_client import ApiClient

class AuthAPI:
    def __init__(self, client=None):
        self.client = client or ApiClient()

    def login(self, email="jun@vivalink.com.cn", password="Jun@1234",tenantId="019cdbd3-4741-752e-bf34-9e436d752aa5",siteId="019cdbd3-4741-753e-a233-bd8b052c7790"):
        resp = self.client.post("/api/backend/authentication", json={"strategy":"local","email":email,"password":password,"request":"","tenantId":tenantId,"siteId":siteId})
        return resp["data"]["accessToken"]

    def get_token(self, email="jun@vivalink.com.cn", password="Jun@1234",tenantId="019cdbd3-4741-752e-bf34-9e436d752aa5",siteId="019cdbd3-4741-753e-a233-bd8b052c7790"):
        resp = self.client.post("/api/backend/authentication", json={"strategy":"local","email":email,"password":password,"request":"","tenantId":tenantId,"siteId":siteId})
        return resp["accessToken"]