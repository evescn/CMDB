from conf import settings


class BasePlugin:
    def __init__(self):
        self.debug = settings.DEBUG
        self.file_path = settings.FILE_PATH

    def get_os(self, handler, hostname=None):
        # 测试模式，直接设置为 Darwin
        host_name = handler.cmd('uname', hostname).strip()
        # host_name = 'Linux'

        if host_name == 'Linux':
            return 'linux'
        elif host_name == 'Darwin':
            return 'darwin'
        else:
            return 'win'

    def process(self, handler, hostname=None):
        # 判断操作系统
        os = self.get_os(handler, hostname)
        # print('os=', os)

        # 反射
        func = getattr(self, os)
        return func(handler, hostname)

    def win(self, handler, hostname=None):
        raise NotImplementedError('win must be Implemented')

    def linux(self, command, hostname=None):
        raise NotImplementedError('linux must be Implemented')
