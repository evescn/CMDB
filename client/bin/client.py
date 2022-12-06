import os, sys
from conf import settings

print(os.path.abspath(__file__))
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, settings.BASE_DIR)
from core.main import run

if __name__ == '__main__':
    run()
