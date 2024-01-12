#!/usr/bin/python3
""" Generates a .tgz archive and deploys it to web servers. """
from datetime import datetime
from fabric.api import local, put, run, env
import os

env.hosts = ['54.236.27.95', '54.237.18.67']
env.user = "ubuntu"
env.key_filename = "~/RSA_public_key"

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        if not os.path.exists("versions"):
            local('mkdir -p versions')
        now = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = 'versions/web_static_' + now + '.tgz'
        local('tar -czvf ' + file_name + ' -C web_static .')
        return file_name
    except Exception:
        return None

def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        file_name = os.path.basename(archive_path)
        name = file_name.split('.')[0]
        release_path = "/data/web_static/releases/" + name
        run("mkdir -p " + release_path)
        run("tar -xzf /tmp/" + file_name + " -C " + release_path)
        run("rm /tmp/" + file_name)
        run("rm -rf /data/web_static/current")
        run("ln -s " + release_path + " /data/web_static/current")
        return True
    except Exception:
        return False

def deploy():
    """ Creates and distributes an archive to web servers. """
    archive_path = do_pack()
    return False if archive_path is None else do_deploy(archive_path)
