from .base import BaseHandler


class SaltHandler(BaseHandler):

    def handler(self):
        print('salt')
        # 采集资产信息 cpu disk memory base
        from ..plugins import get_server_info
        info = get_server_info(self)
        print(info)

        # 向 API 汇报资产

    def cmd(self, command, hostname):
        import salt.client
        local = salt.client.LocalClient()
        result = local.cmd(hostname, 'cmd.run', [command])
        return result
