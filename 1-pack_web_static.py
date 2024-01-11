#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        if not os.path.exists("versions"):
            local(f'mkdir -p versions')

        now = datetime.now()
        file_name = f"versions/web_static_{now.strftime('%Y%m%d%H%M%S')}.tgz"
        local(f'tar -czvf {file_name} -C web_static .')

        return file_name
    except Exception as e:
        return None
