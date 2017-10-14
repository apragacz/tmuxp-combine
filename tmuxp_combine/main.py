from __future__ import print_function, unicode_literals

import argparse
import sys

from tmuxp_combine import commands
from tmuxp_combine.exceptions import TMuxPCombineError
from tmuxp_combine.parser_utils import add_subcommands


def main():
    parser = argparse.ArgumentParser()
    add_subcommands(parser, commands)

    args = parser.parse_args()

    cmd = args.func
    cmd_kwargs = vars(args)
    cmd_kwargs.pop('func')
    try:
        cmd(**cmd_kwargs)
    except TMuxPCombineError as exc:
        print(
            'tmuxp-combine: error: {exc.message}'.format(exc=exc),
            file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
