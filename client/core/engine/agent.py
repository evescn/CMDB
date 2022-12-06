from .base import BaseHandler
from conf import settings
import requests
import json

class AgentHandler(BaseHandler):

    def handler(self):
        # 采集资产信息 cpu disk memory base
        from ..plugins import get_server_info
        info = get_server_info(self)
        print(info)

        # 向 API 汇报资产
        response = requests.post(
            url=settings.ASSET_URL,
            # data=info
            # json=info
            data=json.dumps(info).encode('utf-8'),
            # rest_ful 接口新增
            headers={'Content-Type': 'application/json'},
        )
        print(response.json(), type(response.json()))

        # print(response.content, type(response.content))
        # print(response.text, type(response.text))
        # print(response.json(), type(response.json()))

    def cmd(self, command, hostname=None):
        import subprocess
        result = subprocess.getoutput(command)
        return result
