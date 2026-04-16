#!/bin/bash
./sbin/nginx -s stop
sleep 3
./sbin/nginx
./sbin/nginx -s reload
echo "启动nginx成功"
exit