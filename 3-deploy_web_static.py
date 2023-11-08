#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates and
distributes an archive to your web servers, using the function deploy
"""


from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy
from fabric.api import env, local, put, run
import os
import datetime
env.hosts = ['100.25.144.173', '54.160.65.154']


def deploy():
    """
    Return the return value of do_deploy
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    if do_deploy(archive_path):
        return True
    return False
