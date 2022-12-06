from .base import BasePlugin
import os
import traceback
from lib.response import BaseResponse


class Cpu(BasePlugin):
    def win(self, handler, hostname=None):
        """
        agent subprocess
        ssh Parmiko
        salt salt
        ansible ansible
        :return:
        """

        result = handler.cmd("", hostname)
        return result

    def linux(self, handler, hostname=None):
        """
        agent subprocess
        ssh Parmiko
        salt salt
        ansible ansible
        :return:
        """

        response = BaseResponse()
        # response = {'status': True, 'error': None, 'data': None}
        try:
            if self.debug:
                with open(os.path.join(self.file_path, 'cpuinfo.out'), encoding='utf-8') as f:
                    ret = f.read()
            else:
                ret = handler.cmd('cat /proc/cpuinfo', hostname)
            ret = self.parse(ret)
            response.data = ret
        except Exception:
            error = traceback.format_exc()  # 详细的错误
            response.status = False
            response.error = error
        return response.dict

    def darwin(self, handler, hostname=None):
        """
        agent subprocess
        ssh Parmiko
        salt salt
        ansible ansible
        :return:
        """
        response = BaseResponse()
        # result = {'status': True, 'error': None, 'data': None}
        try:
            if self.debug:
                with open(os.path.join(self.file_path, 'cpuinfo.out'), encoding='utf-8') as f:
                    result = f.read()
            else:
                result = handler.cmd("top -l 1 | grep 'CPU usage'", hostname)
            result = self.parse(result)
            response.data = result

        except Exception:
            error = traceback.format_exc()  # 详细的错误
            response.status = False
            response.error = error

        return response.dict

    @staticmethod
    def parse(content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        response = {'cpu_count': 0, 'cpu_physical_count': 0, 'cpu_model': ''}

        cpu_physical_set = set()
        content = content.strip()
        for item in content.split('\n\n'):
            for row_line in item.split('\n'):
                key, value = row_line.split(':')
                key = key.strip()
                if key == 'processor':
                    response['cpu_count'] += 1
                elif key == 'physical id':
                    cpu_physical_set.add(value)
                elif key == 'model name':
                    if not response['cpu_model']:
                        response['cpu_model'] = value
        response['cpu_physical_count'] = len(cpu_physical_set)

        return response
