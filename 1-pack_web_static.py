#!/usr/bin/python3
''' A fabric script that generates
a .tgz archive from content of web_static folder
'''


from fabric.api import local
from datetime import datetime
import os


def do_pack():
    ''' generate an archive'''

    dir_name = 'web_static'
    if not os.path.exists(dir_name):
        return None
    date = datetime.now()
    date_string = date.strftime('%Y%m%d%H%M%S')
    dir_name = dir_name + '_' + date_string
    if not os.path.exists('versions'):
        local('mkdir versions', capture=False)
    archive_path = 'versions/{}.tgz'.format(dir_name)
    local('tar -cvzf {} web_static'.format(archive_path), capture=False)

    return os.path.abspath(archive_path)
