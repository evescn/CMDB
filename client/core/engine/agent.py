from .base import BaseHandler


class AgentHandler(BaseHandler):

    def handler(self):
        # 采集资产信息 cpu disk memory base
        from ..plugins import get_server_info
        ret = get_server_info(self)
        print(ret)

        # 向 API 汇报资产

    def cmd(self, command, hostname=None):
        import subprocess
        result = subprocess.getoutput(command)
        return result
