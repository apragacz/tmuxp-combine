from __future__ import print_function, unicode_literals

from tmuxp_combine.core import get_window_names


def prepare_parser(parser):
    parser.add_argument('project')


def command(project):
    window_names = get_window_names(project)
    for name in window_names:
        print(name)
