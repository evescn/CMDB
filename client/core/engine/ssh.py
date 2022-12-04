from .base import BaseHandler
from conf import settings


class SSHHandler(BaseHandler):

    def handler(self):
        # 采集资产信息 cpu disk memory base
        from ..plugins.disk import get_disk
        data = get_disk(self)
        print(data)

        # 向 API 汇报资产

    def cmd(self, command, hostname):
        import paramiko

        private_key = paramiko.RSAKey.from_private_key_file(settings.SSH_KEY)

        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(
            hostname=hostname,
            port=settings.SSH_PORT,
            username=settings.SSH_USERNAME,
            key=private_key,
            password=settings.SSH_PASSWORD
        )

        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()

        # 关闭连接
        ssh.close()

        return result
