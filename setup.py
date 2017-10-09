import os.path
import re

from setuptools import find_packages, setup

ROOT_DIR = os.path.dirname(__file__)


def read_contents(local_filepath):
    with open(os.path.join(ROOT_DIR, local_filepath)) as f:
        return f.read()


def get_requirements(requirements_filepath):
    '''
    Return list of this package requirements via local filepath.
    '''
    return read_contents(requirements_filepath).split('\n')


def get_version(package):
    '''
    Return package version as listed in `__version__` in `init.py`.
    '''
    init_py = read_contents(os.path.join(package, '__init__.py'))
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_long_description(markdown_filepath):
    '''
    Return the long description in RST format, when possible.
    '''
    try:
        import pypandoc
        return pypandoc.convert(markdown_filepath, 'rst')
    except ImportError:
        return read_contents(markdown_filepath)


setup(
    name='tmuxp-combine',
    version=get_version('tmuxp_combine'),
    packages=find_packages(exclude=['tests.*', 'tests']),
    author='Andrzej Pragacz',
    author_email='apragacz@o2.pl',
    description=(
        'A tool for combining tmuxp configs'
    ),
    license='MIT',
    keywords='tmux tmuxp cli',
    long_description=get_long_description('README.md'),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'tmuxp-combine = tmuxp_combine.main:main',
        ],
    },
    install_requires=get_requirements('requirements.txt'),
    url='https://github.com/szopu/tmuxp-combine',
)
