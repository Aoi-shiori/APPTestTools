#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/23 16:51
@File: api_client.py
@IDE: PyCharm
@Description: 
"""

import requests
import json
from config.settings import API_BASE_URL, API_TIMEOUT
from utils.logger import get_logger

logger = get_logger()

class ApiClient:
    def __init__(self, base_url=None):
        self.base_url = base_url or API_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def set_token(self, token):
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def request(self, method, path, **kwargs):
        url = f"{self.base_url}{path}"
        kwargs.setdefault("timeout", API_TIMEOUT)
        logger.info(f"API {method.upper()} {url} | params={kwargs.get('params')} | data={kwargs.get('json')}")
        resp = self.session.request(method, url, **kwargs)
        logger.info(f"Response status: {resp.status_code}, body: {resp.text[:200]}")
        resp.raise_for_status()
        return resp.json()

    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)
    def put(self, path, **kwargs):
        return self.request("PUT", path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)

    def patch(self, path, **kwargs):
        return self.request("PATCH", path, **kwargs)