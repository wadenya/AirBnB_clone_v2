#!/usr/bin/python3
"""Compress before sending"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Packs web_static files into .tgz file.
    """
 
    # Get the current time in the format yearmonthdayhourminutesecond
    time_now = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = "web_static_{}.tgz".format(time_now)
    archive_path = "versions/{}".format(archive_name)

    # Create directory if it doesn't exist
    local("mkdir -p versions")

    # Create the tarball
    archive_command = local("tar -cvzf {} web_static".format(archive_path))

    # Check if the command was successful
    if archive_command.succeeded:
        return archive_path
    return None
