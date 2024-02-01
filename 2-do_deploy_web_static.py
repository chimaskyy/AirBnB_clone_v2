#!/usr/bin/python3
""" A fabric script that generates
a .tgz archive from content of web_static folder
"""


from fabric.api import local, run, put, env
from datetime import datetime
import os

env.hosts = ["54.175.8.50", "54.237.39.190"]
env.user = "ubuntu"
env.key = "~/.ssh/id_rsa"


def do_pack():
    """generate an archive"""

    dir_name = "web_static"
    if not os.path.exists(dir_name):
        return None
    date = datetime.now()
    date_string = date.strftime("%Y%m%d%H%M%S")
    dir_name = dir_name + date_string
    if not os.path.exists("versions"):
        local("mkdir versions", capture=False)
    archive_path = "versions/{}.tgz".format(dir_name)
    local("tar -cvzf {} web_static".format(archive_path), capture=False)

    return os.path.abspath(archive_path)


def do_deploy(archive_path):
    """Deploy archive to server"""

    if not os.path.exists(archive_path):
        return False
    try:
        # upload achieved path to tem dir of server
        put(local_path=archive_path, remote_path='/tmp/')
        path_ = os.path.basename(archive_path)
        path_without_ext = os.path.splitext(path_)[0]
        # path_ = archive_path.split('/')[-1]
        # path_without_ext = path_.replace('.tgz','')
        
        # uncompress file
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(path_, path_without_ext))
        # Delete archive from web server
        run("rm /tmp/{}".format(path_))
        run("mv /data/web_static/releases/{}/web_static/*\
                /data/web_static/releases/{}/".format(path_, path_without_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(path_))

        # remove symbolic link
        run("rm -rf /data/web_static/current")
        # create new symlink linked to the new server config
        run("ln -sf /data/web_static/releases/{} /data/web_static/current".format(path_without_ext))
        return True
    except Exception as e:
        print (f"Erro: {e}")
        return False


