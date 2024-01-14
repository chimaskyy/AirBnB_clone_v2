#!/usr/bin/python3
"""
Deploys archive to remote server.
"""

from fabric.api import put, run, env
import os

env.hosts = ['18.234.253.75', '54.174.123.116']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    This functions transfers compressed web_static content to
    the specified hosts server, decompresses them and deploy then
    for the web_server to serve

    Argument: string -> path to archived contents
    return: True if all operations were successful
            False if any failed or archive passed doesn't exist.
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
        print("New version deployed")
        return True
    except Exception as e:
        print(f"Deployment Failed")
        return False
