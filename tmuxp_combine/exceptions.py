from __future__ import print_function, unicode_literals


class TMuxPCombineError(Exception):
    pass


class ConfigDirectoryNotFound(TMuxPCombineError):

    def __init__(self, dir_path):
        super(ConfigDirectoryNotFound, self).__init__(
            'Config directory not found: {dir_path}'.format(
                dir_path=dir_path))
        self.dir_path = dir_path


class ProjectNotFound(TMuxPCombineError):

    def __init__(self, project_name):
        super(ProjectNotFound, self).__init__(
            'Project not found: {project_name}'.format(
                project_name=project_name))
        self.project_name = project_name


class ConfigNotFound(TMuxPCombineError):

    def __init__(self, config_path):
        super(ConfigNotFound, self).__init__(
            'Config not found: {config_path}'.format(config_path=config_path))
        self.config_path = config_path
