#!/usr/bin/env python
# -*- coding: utf-8 -*-

from invoke.util import cd

__author__ = 'Guowei'

import os, re

from datetime import datetime
from fabric.api import *

env.user = 'guowei'
env.sudo_user = 'root'
env.hosts = ['47.95.231.61']

db_user = 'root'
db_password = '123456'

_TAR_FILE = 'dist-WebApp.tar.gz'

_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE

_REMOTE_BASE_DIR = '/srv/WebApp'

def _current_path():
    return os.path.abspath('.')

def _now():
    return datetime.now().strftime('%y-%m-%d_%H.%M.%S')

def backup():
    '''
    Dump entire database on server and backup to local.
    '''
    dt = _now()
    f = 'backup-awesome-%s.sql' % dt
    with cd('/tmp'):
        run('mysqldump --user=%s --password=%s --skip-opt --add-drop-table --default-character-set=utf8 --quick awesome > %s' % (db_user, db_password, f))
        run('tar -czvf %s.tar.gz %s' % (f, f))
        get('%s.tar.gz' % f, '%s/backup/' % _current_path())
        run('rm -f %s' % f)
        run('rm -f %s.tar.gz' % f)
