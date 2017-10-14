from __future__ import print_function, unicode_literals

import os
import tempfile

from tmuxp_combine.core import combine_configs, dump_config_yaml_to_str_file


def prepare_parser(parser):
    parser.add_argument('session')
    parser.add_argument('-w', '--window', dest='windows', action='append')


def command(session, windows):
    cfg = combine_configs(session, windows)
    with tempfile.NamedTemporaryFile(
            'wt',
            prefix='tmuxp-combined-',
            suffix='.yml') as f:
        cfg_path = f.name
        dump_config_yaml_to_str_file(cfg, f)
        f.flush()
        os.system('tmuxp load {cfg_path}'.format(cfg_path=cfg_path))
