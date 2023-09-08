#!/usr/bin/python3
"""Compress before sending"""

from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once

@runs_once
def create_archive():
    '''Package web_static directory into timestamped .tgz archive'''
    local("mkdir -p archives")
    archive_path = ("archives/content_{}.tgz"
                    .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    tar_command = local("tar -cvzf {} web_static"
                        .format(archive_path))

    if tar_command.failed:
        return None
    return archive_path
