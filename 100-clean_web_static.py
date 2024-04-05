#!/usr/bin/python3
"""
    Fabric script for cleaning up old archives
"""
from fabric.api import env, run, local
from datetime import datetime
import os

env.hosts = ['100.27.10.232', '54.144.152.144']


def do_clean(number=0):
    """
        Cleans up old archives
    """
    try:
        number = int(number)
        if number < 0:
            number = 0

        # Local cleanup
        local("mkdir -p versions")
        local_archives = local("ls -t versions", capture=True).split('\n')
        if len(local_archives) > number:
            archives_to_delete = local_archives[number:]
            for archive in archives_to_delete:
                local("rm -f versions/{}".format(archive))

        # Remote cleanup
        remote_archives = run("ls -t /data/web_static/releases").split('\n')
        if len(remote_archives) > number:
            archives_to_delete = remote_archives[number:]
            for archive in archives_to_delete:
                run("rm -rf /data/web_static/releases/{}".format(archive))

        return True
    except Exception as e:
        print("An error occurred:", str(e))
        return False


if __name__ == "__main__":
    do_clean()
