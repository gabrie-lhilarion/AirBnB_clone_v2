#!/usr/bin/python3
"""
    Fabric script generates tgz archive from contents of web_static
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        Generates a .tgz archive from contents of web_static
    """
    time = datetime.now(datetime.UTC).strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(file_name))
        return file_name
    except:
        return None
