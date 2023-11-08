#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""


from fabric.api import env, local, put, run
import os
import datetime
env.hosts = ['100.25.144.173', '54.160.65.154']


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


def do_deploy(archive_path):
    """
    Returns False if the file at the path archive_path doesn’t exist
    """
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        arg_1 = filename.split(".")[0]
        dir_path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(dir_path, arg_1))
        run("tar -xzf /tmp/{} -C {}{}/".format(filename, dir_path, arg_1))
        run("rm /tmp/{}".format(filename))
        run("mv {0}{1}/web_static/* {0}{1}/".format(dir_path, arg_1))
        run("rm -rf {}{}/web_static".format(dir_path, arg_1))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dir_path, arg_1))
        return True
    except Exception as e:
        return False
