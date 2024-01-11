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

        now = datetime.now()
        file_name = "versions/web_static_{}.tgz".format(
            now.strftime('%Y%m%d%H%M%S'))
        local('tar -czvf {} -C web_static .'.format(file_name))

        return file_name
    except Exception as e:
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        # Uncompress the archive
        file_name = os.path.basename(archive_path)
        name = file_name.split('.')[0]
        release_path = "/data/web_static/releases/{}".format(name)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, release_path))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_name))

        # Delete the symbolic link
        run("rm -rf /data/web_static/current")

        # Create new the symbolic link
        current_path = "/data/web_static/current"
        run("ln -s {} {}".format(release_path, current_path))

        return True

    except Exception:
        return False


def deploy():
    """ Creates and distributes an archive to web servers. """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
