from conf import settings
from lib.import_class import get_class
import importlib


def get_server_info(handler, hostname=None):
    for name, string in settings.ENGINE_DICT.items():
        # print(name, string)
        cls = get_class(string)
        print(cls)
        obj = cls()
        ret = obj.process(handler, hostname=None)
        print(ret)
