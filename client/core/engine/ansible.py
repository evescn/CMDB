from .base import BaseHandler


class AnsibleHandler(BaseHandler):

    def handler(self):
        print('Ansible')

    def cmd(self, command, hostname):
        pass
