#!/usr/bin/python3
"""
Deploys archive to remote server.
"""
from fabric.api import put, run, env
from datetime import datatime
import os

env.hosts = ['18.234.253.75', '54.174.123.116']

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
        run('echo "Holberton School" > /data/web_static/current/my_index.html')
        run('mv /data/web_static/releases/{}/web_static/* '
            .format(new_release) + '/data/web_static/current')
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(new_release))
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
