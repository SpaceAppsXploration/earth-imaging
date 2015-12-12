"""
Set environment variables (online or offline mode).
"""

import os

__author__ = 'Lorenzo'


ENV = {
    'offline': {
        '_SERVICE': 'http://localhost:8080/',
        '_DEBUG': True
    },
    'online': {
        '_SERVICE': 'http://earth-imaging.appspot.com/',
        '_DEBUG': True
    }
}


def set_env_variables():
    """
    Set different variables if the environment is running on a local machine
    or in the sandbox.
    :return: a tuple with a string and a boolean
    """
    if 'SERVER_SOFTWARE' not in os.environ \
            or os.environ['SERVER_SOFTWARE'].startswith('Development'):
        # the development server is running
        _SERVICE, _DEBUG = ENV['offline']['_SERVICE'], ENV['offline']['_DEBUG']

    else:
        # the online sandboxed environment is running
        _SERVICE, _DEBUG = ENV['online']['_SERVICE'], ENV['online']['_DEBUG']

    return _SERVICE, _DEBUG

SERVICE, DEBUG = set_env_variables()
