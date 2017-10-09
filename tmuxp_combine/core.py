from __future__ import print_function, unicode_literals

import os

import yaml

from tmuxp_combine.exceptions import (
    ConfigDirectoryNotFound,
    ConfigNotFound,
    SessionNotFound
)


def load_yaml_from_filepath(path):
    try:
        with open(path, 'r') as f:
            return yaml.safe_load(f.read())
    except EnvironmentError:
        raise ConfigNotFound(path)


def get_config_path(config_path=None):
    if config_path is None:
        home_path = os.environ['HOME']
        config_path = os.path.join(home_path, '.tmuxp-combine')
    if not os.path.exists(config_path):
        raise ConfigDirectoryNotFound(config_path)
    return config_path


def get_session_path(session_name, config_path=None):
    config_path = get_config_path(config_path=config_path)
    return os.path.join(config_path, session_name)


def _get_windows_path(session_path):
    return os.path.join(session_path, 'windows')


def get_window_names(session_name, config_path=None):
    session_path = get_session_path(session_name, config_path=config_path)
    windows_path = _get_windows_path(session_path)
    try:
        names = os.listdir(windows_path)
    except EnvironmentError:
        raise SessionNotFound(session_name)

    splits = [os.path.splitext(name) for name in names]
    return [name for name, ext in splits if ext == '.yml']


def get_session_names(config_path=None):
    config_path = get_config_path(config_path=config_path)
    names = [
        name for name in os.listdir(config_path)
        if name not in {'.', '..'}]
    return names


def combine_configs(session_name, window_names):
    session_path = get_session_path(session_name)
    windows_path = _get_windows_path(session_path)
    session_base_cfg_path = os.path.join(session_path, 'base.yml')
    cfg = load_yaml_from_filepath(session_base_cfg_path)
    windows_cfg = []

    if not window_names:
        window_names = get_window_names(session_name)

    for window_name in window_names:
        window_cfg_path = os.path.join(windows_path, window_name + '.yml')
        windows_cfg.append(load_yaml_from_filepath(window_cfg_path))

    cfg['windows'] = windows_cfg
    return cfg


def get_config_yaml(cfg):
    return yaml.safe_dump(cfg)


def dump_config_yaml_to_str_file(cfg, f):
    yaml.safe_dump(cfg, stream=f)
