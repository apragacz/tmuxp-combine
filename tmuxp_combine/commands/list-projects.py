from __future__ import print_function, unicode_literals

from tmuxp_combine.core import get_project_names


def command():
    project_names = get_project_names()
    for name in project_names:
        print(name)
