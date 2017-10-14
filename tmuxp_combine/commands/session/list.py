from __future__ import print_function, unicode_literals

from tmuxp_combine.core import get_session_names


def command():
    session_names = get_session_names()
    for name in session_names:
        print(name)
