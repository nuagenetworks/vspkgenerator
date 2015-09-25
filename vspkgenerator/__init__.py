# -*- coding:utf-8 -*-

import pkg_resources
import subprocess
import sys


def generate_vspk(argv=sys.argv):
    """
    """
    path = pkg_resources.resource_filename('vspkgenerator', 'conf/config.ini')
    subprocess.call(["generate-sdk", "--config", path] + argv[1:])


def generate_vspkdoc(argv=sys.argv):
    """
    """
    path = pkg_resources.resource_filename('vspkgenerator', 'conf/config.ini')
    subprocess.call(["generate-sdkdoc", "--config", path] + argv[1:])


def generate_vsd_apidoc(argv=sys.argv):
    """
    """
    path = pkg_resources.resource_filename('vspkgenerator', 'conf/config.ini')
    subprocess.call(["generate-apidoc", "--config", path] + argv[1:])