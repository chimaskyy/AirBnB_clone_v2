#!/usr/bin/python3
"""
Deploys archive to remote server.
"""
from fabric.api import put, run, env, local
from datetime import datetime
import os

env.hosts = ['18.234.253.75', '54.174.123.116']


def do_pack():
    """
    genrates archive from web_static directory.
    """

    dir_name = 'web_static'
    if not os.path.exists(dir_name):
        return None
    date = datetime.now()
    date_string = date.strftime('%Y%m%d%H%M%S')
    dir_name = dir_name + date_string
    if not os.path.exists('versions'):
        local('mkdir versions', capture=False)
    archive_path = 'versions/{}.tgz'.format(dir_name)
    local('tar -cvzf {} web_static'.format(archive_path), capture=False)

    return os.path.abspath(archive_path)


def do_deploy(archive_path):
    """
    deploy function

    archive_path: path to the archive on the local machine
    return: True if operations worked correctly
            False if operations failed or archive_path does not exist
    """

    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the remote server
        put(local_path=archive_path, remote_path='/tmp/')

        # Decompresses Archive
        new_release = archive_path.split('/')[-1].replace('.tgz', '')
        run('mkdir -p /data/web_static/releases/{}'.format(new_release))
        run('tar -xf /tmp/{} -C /data/web_static/releases/{}'
            .format(archive_path.split('/')[-1], new_release))
        run('rm /tmp/{}'.format(archive_path.split('/')[-1]))

        # Updates Symbolic link
        run('rm /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(new_release))
        run('mv /data/web_static/releases/{}/web_static/* '
            .format(new_release) + '/data/web_static/current')
        run('echo "Holberton School" > /data/web_static/current/my_index.html')
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(new_release))
        print('New version deployed!')
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def deploy():
    """ Full deployment function """

    archive = do_pack()

    if archive:
        return do_deploy(archive)
    else:
        return False
