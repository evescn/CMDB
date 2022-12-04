class Memory:
    def process(self, handler, hostname=None):
        """
        agent subprocess
        ssh Parmiko
        salt salt
        ansible ansible
        :return:
        """

        result = handler.cmd('df -h', hostname)
        return result