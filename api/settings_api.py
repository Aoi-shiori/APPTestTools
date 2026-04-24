#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/23 17:08
@File: settings_api.py
@IDE: PyCharm
@Description: 
"""
from time import sleep

from api.auth_api import AuthAPI
from core.api_client import ApiClient
from utils.logger import get_logger

logger = get_logger()



class SettingsAPI(ApiClient):
    def __init__(self, base_url=None):
        super().__init__(base_url)
        self.auth_api = AuthAPI()
        self.token = self.auth_api.get_token()
        self.set_token(self.token)

    def get_sites(self):
        resp = self.get("/api/backend/sites")
        logger.info(f"Response total: {resp.get('total')}, body:{resp.get('data')} ")
        return resp["data"]

    def get_site_id(self,site_name):
        sites = self.get_sites()
        site_id = next((site["id"] for site in sites if site["name"] == site_name), None)
        return site_id

    def delete_site(self, site_name):
        site_id=self.get_site_id(site_name)
        resp = self.delete(f"/api/backend/sites/{site_id}")
        return resp

    def add_site(self, site_name="first3"):
        resp = self.post("/api/backend/sites",
                         json={"name":site_name,"displayName":site_name,"address":"","countryCode":"US"})
        return resp
