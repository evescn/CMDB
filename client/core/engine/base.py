class BaseHandler():

    def handler(self):
        raise NotImplementedError('handler must be Implemented')

    def cmd(self, command, hostname):
        raise NotImplementedError('handler must be Implemented')
