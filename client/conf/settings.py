ENGINE = 'agent'

ENGINE_DICT = {
    'agent': 'core.engine.agent.AgentHandler',
    'salt': 'core.engine.salt.SaltHandler',
    'ssh': 'core.engine.ssh.SSHHandler',
    'ansible': 'core.engine.ansible.AnsibleHandler',
}

PLUGINS_DICT = {
    # 'cpu': 'core.plugins.cpu.Cpu',
    'disk': 'core.plugins.disk.Disk',
    # 'memory': 'core.plugins.memory.Memory',
    'nic': 'core.plugins.nic.Nic',
}

SSH_PORT = 22
SSH_USERNAME = 'root'
SSH_PASSWORD = ''
SSH_KEY = ''