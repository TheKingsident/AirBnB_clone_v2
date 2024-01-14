#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        if not os.path.exists("versions"):
            local('mkdir -p versions')

        now = datetime.now()
        file_name = "versions/web_static_{}.tgz".format(
            now.strftime('%Y%m%d%H%M%S'))
        # Archive the web_static folder itself, not just its contents
        local('tar -czvf {} web_static'.format(file_name))

        return file_name
    except Exception as e:
        return None
