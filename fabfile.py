"""
Fabfile for DCUO LFG.
"""

import os

from fabric.api import *

def clean():
    """Clean up after a local build."""
    local('rm -rf bin develop-eggs downloads eggs include lib parts '
          '.installed.cfg .Python src/dcuolfg.egg-info')
    local('find . -name \*.pyc|xargs rm')

def init():
    """Initialize virtualenv and bootstap."""
    if not os.path.isdir('bin'):
        local('virtualenv --no-site-packages .', capture=False)
        local('./bin/python bootstrap.py', capture=False)

def devel():
    """Create a self-contained development build."""
    init()
    local('./bin/buildout install dev', capture=False)

