#!/usr/bin/python3
'''Fabric script to deploy web_static content to web servers'''

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['3.89.160.21', '54.197.132.144']

def do_deploy(archive_path):
    '''deploys an archive to the web servers'''
    
    # Check if archive path exists
    if not exists(archive_path):
        return False
    
    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        
        # Get the filename without extension
        archive_name = archive_path.split('/')[-1]
        without_tgz = archive_name.split('.')[0]
        release_path = "/data/web_static/releases/{}".format(without_tgz)

        # Uncompress the archive to the target directory on the web server
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, release_path))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_name))

        # Move the files from web_static_* to web_static
        run("mv {}/web_static/* {}".format(release_path, release_path))
        
        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")
        
        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_path))
        
        return True
    except:
        return False

