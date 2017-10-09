from __future__ import print_function, unicode_literals


class TMuxPCombineError(Exception):
    pass


class ConfigDirectoryNotFound(TMuxPCombineError):

    def __init__(self, dir_path):
        super(ConfigDirectoryNotFound, self).__init__(
            'Config directory not found: {dir_path}'.format(
                dir_path=dir_path))
        self.dir_path = dir_path


class SessionNotFound(TMuxPCombineError):

    def __init__(self, session_name):
        super(SessionNotFound, self).__init__(
            'Session not found: {session_name}'.format(
                session_name=session_name))
        self.session_name = session_name


class ConfigNotFound(TMuxPCombineError):

    def __init__(self, config_path):
        super(ConfigNotFound, self).__init__(
            'Config not found: {config_path}'.format(config_path=config_path))
        self.config_path = config_path
