#!/usr/bin/python3
"""
    Fabric script that distributes an archive to my web servers
"""
from fabric.api import env, put, run
import os

env.hosts = ['66.70.184.249', '54.210.138.75']

def do_deploy(archive_path):
    """
        using fabric to distribute archive
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        folder_name = os.path.splitext(archive_filename)[0]
        remote_tmp_path = "/tmp/{}".format(archive_filename)
        remote_release_path = "/data/web_static/releases/{}".format(folder_name)

        put(archive_path, remote_tmp_path, use_sudo=True)

        run("mkdir -p {}".format(remote_release_path))
        run("tar -xzf {} -C {}".format(remote_tmp_path, remote_release_path))
        run("rm {}".format(remote_tmp_path))
        run("mv {}/web_static/* {}".format(remote_release_path, remote_release_path))
        run("rm -rf {}/web_static".format(remote_release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(remote_release_path))

        return True
    except Exception as e:
        print("An error occurred:", str(e))
        return False
