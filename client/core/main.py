from conf import settings
from lib.import_class import get_class


def run():
    # 反射
    cls = get_class(settings.ENGINE_DICT.get(settings.ENGINE))
    obj = cls()
    obj.handler()
