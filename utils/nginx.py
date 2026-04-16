import subprocess
import time

import psutil
from utils.logger import get_logger
import config.settings as conf
from utils.getIP import get_local_ip
import os
import stat

logs = get_logger(__name__)


class Nginx:
    def __init__(self):
        self.nginx_dir = f"{conf.NGINX_DIR}"
        logs.info(f"Nginx目录：{self.nginx_dir}")
        self.process_name = "nginx"

    def dosomething(self):
        if self.process_exists(process_name=self.process_name):
            self.stop_nginx()
            self.start_nginx()
            self.restart_nginx()
            # 端口固定为8112，可以在ningx.conf中修改
            logs.info(f"Nginx Allure报告服务地址：http://{get_local_ip()}:8112")
        else:
            self.start_nginx()
            time.sleep(2)
            if self.process_exists(process_name=self.process_name):
                logs.info(f"Nginx Allure报告服务地址：http://{get_local_ip()}:8112")
            else:
                logs.error("Nginx服务启动失败，请检查Nginx配置或者Nginx是否安装")

    def process_exists(self, process_name):

        # 转换进程名为小写，因为psutil通常会返回小写的进程名
        process_name = process_name.lower()
        for proc in psutil.process_iter(['name']):
            try:
                # 过滤出匹配进程名的进程
                if proc.info['name'].lower() == process_name:
                    return True
            except psutil.NoSuchProcess:
                pass
        return False



    def start_nginx(self):
        nginx_bin = os.path.join(self.nginx_dir, "sbin", "nginx")

        # 检查 nginx 二进制是否存在
        if not os.path.isfile(nginx_bin):
            logs.error(f"nginx 二进制文件不存在: {nginx_bin}")
            return False

        # 检查并添加执行权限
        if not os.access(nginx_bin, os.X_OK):
            logs.warning(f"nginx 缺少执行权限，正在添加...")
            try:
                # 添加所有者、组、其他人的执行权限 (755)
                os.chmod(nginx_bin, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
                logs.info(f"已为 {nginx_bin} 添加执行权限")
            except Exception as e:
                logs.error(f"添加执行权限失败: {e}")
                return False

        # 执行启动脚本（确保 start.sh 也有执行权限）
        start_script = os.path.join(self.nginx_dir, "start.sh")
        if not os.path.isfile(start_script):
            logs.error(f"启动脚本不存在: {start_script}")
            return False

        if not os.access(start_script, os.X_OK):
            os.chmod(start_script, 0o755)

        result = subprocess.run([start_script], cwd=self.nginx_dir, text=True)
        if result.returncode != 0:
            logs.error(f"启动脚本执行失败，返回码: {result.returncode}")
            return False

        logs.info("Nginx 启动脚本执行完毕，等待服务就绪...")

        # 可选：增加健康检查，确认 nginx 进程真的启动了
        import time
        time.sleep(2)  # 给 nginx 一点启动时间
        if self.check_nginx_running():
            logs.info("Nginx 服务启动成功")
            return True
        else:
            logs.error("Nginx 服务启动失败，请检查配置文件或端口占用")
            return False

    def check_nginx_running(self):
        """检查 nginx 进程是否存在"""
        try:
            result = subprocess.run(["pgrep", "-f", "nginx"], capture_output=True, text=True)
            return result.returncode == 0
        except Exception:
            return False


    def stop_nginx(self):
        logs.info("停止Nginx服务...")

        # 运行一个Bash命令
        command = "nginx -s stop"
        subprocess.run(command,cwd=self.nginx_dir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logs.info("Nginx服务已停止...")

    def restart_nginx(self):
        logs.info("重启Nginx服务...")

        # 运行一个Bash命令
        command = "nginx -s reload"
        subprocess.run(command,cwd=self.nginx_dir,  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logs.info("Nginx服务已重启...")

if __name__ == '__main__':
    nginx = Nginx()
    # exists=nginx.process_exists(process_name=nginx.process_name)
    # print(exists)
    nginx.dosomething()