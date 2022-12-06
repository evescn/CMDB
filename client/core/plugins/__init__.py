from conf import settings
from lib.import_class import get_class
import importlib


def get_server_info(handler, hostname=None):
    info = {}

    for name, string in settings.PLUGINS_DICT.items():
        # 反射
        # print(name, string)
        cls = get_class(string)
        # print(cls)
        obj = cls()
        ret = obj.process(handler, hostname)

        info[name] = ret

    return info