import requests
import json

from conf import settings
import importlib
from lib.import_class import get_class

def run():
    cls = get_class(settings.ENGINE_DICT.get(settings.ENGINE))
    obj = cls()
    obj.handler()


    # print('xxxx')
    # info = {'disk': {'1': {'x': 'x'}},
    #         'cpu': {'xx': {}},
    #         'net': 'xxx',
    #
    #         }
    #
    # response = requests.post(
    #     url='http://127.0.0.1:8000/api/asset/',
    #     # data=info
    #     # json=info
    #     data=json.dumps(info).encode('utf-8')
    # )
    #
    # print(response.content, type(response.content))
    # print(response.text, type(response.text))
    # print(response.json(), type(response.json()))
