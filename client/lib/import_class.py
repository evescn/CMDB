# from conf import settings
import importlib

def get_class(calss_path):
    module_name, cls_name = calss_path.rsplit('.', maxsplit=1)
    # print(module_name, cls_name)
    module = importlib.import_module(module_name)
    cls = getattr(module, cls_name)
    return cls