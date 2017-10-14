from __future__ import print_function, unicode_literals

from tmuxp_combine.core import combine_configs, get_config_yaml


def prepare_parser(parser):
    parser.add_argument('session')
    parser.add_argument('-w', '--window', dest='windows', action='append')


def command(session, windows):
    cfg = combine_configs(session, windows)
    print(get_config_yaml(cfg), end='')
