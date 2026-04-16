#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: APP Test Tools
@Author: guojun
@Email: 391350540@qq.com
@Date: 2026/4/13 17:30
@File: device_manager.py
@IDE: PyCharm
@Description: 
"""
from airtest.core.api import connect_device, device as current_device
from airtest.core.api import G, set_current
from config.settings import DEVICE_CONFIG
from utils.logger import get_logger

logger = get_logger()

class DeviceManager:
    """设备连接与切换管理"""
    _instance = None
    _device = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self, device_uri=None):
        """连接设备，uri示例：Android:/// 或 Android://127.0.0.1:5037/设备号"""
        if not device_uri:
            # 使用默认配置
            cfg = DEVICE_CONFIG["android"]
            device_uri = f"Android:///{cfg['uuid'] if cfg['uuid'] else ''}"
        try:
            self._device = connect_device(device_uri)
            logger.info(f"设备连接成功: {device_uri}")
            return self._device
        except Exception as e:
            logger.error(f"设备连接失败: {e}")
            raise

    def get_device(self):
        if not self._device:
            self.connect()
        return self._device

    def disconnect(self):
        if self._device:
            # Airtest 没有显式的断开方法，清空即可
            self._device = None
            logger.info("设备已断开")

device_mgr = DeviceManager()