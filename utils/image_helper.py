#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/15 15:14
@File: image_helper.py
@IDE: PyCharm
@Description: 
"""
from airtest.core.api import Template
from config.settings import IMAGES_DIR

def get_template(image_name, **kwargs):
    """统一创建 Template 对象，自动添加路径前缀"""
    img_path = str(IMAGES_DIR / image_name)
    return Template(img_path, **kwargs)