import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False
FILE_PATH = os.path.join(BASE_DIR, 'files')

ENGINE = 'ssh'

ENGINE_DICT = {
    'agent': 'core.engine.agent.AgentHandler',
    'salt': 'core.engine.salt.SaltHandler',
    'ssh': 'core.engine.ssh.SSHHandler',
    'ansible': 'core.engine.ansible.AnsibleHandler',
}

PLUGINS_DICT = {
    'basic': 'core.plugins.basic.Basic',
    'main_board': 'core.plugins.main_board.MainBoard',
    'cpu': 'core.plugins.cpu.Cpu',
    'disk': 'core.plugins.disk.Disk',
    'memory': 'core.plugins.memory.Memory',
    'nic': 'core.plugins.nic.Nic',
}

ASSET_URL = 'http://127.0.0.1:8000/api/asset/'

SSH_PORT = 22
SSH_USERNAME = 'root'
SSH_PASSWORD = ''
SSH_KEY = '/Users/evescn/.ssh/id_rsa'