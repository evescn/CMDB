import os, sys

print(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.main import run

if __name__ == '__main__':
    run()
