#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""


from fabric.api import local
import os
import datetime


def do_pack():
    """
    Return the archive path if the archive has been
    correctly generated. Otherwise, return None
    """
    try:
        os.makedirs("versions", exist_ok=True)
        time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(time)
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        return None
