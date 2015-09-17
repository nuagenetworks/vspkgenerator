# -*- coding:utf-8 -*-

import pkg_resources
import subprocess
import sys


def main(argv=sys.argv):
    """
    """
    path = pkg_resources.resource_filename('vspkgenerator', 'vanilla/config.ini')
    print path
    subprocess.call(["generate-sdk", "--config", path] + argv[1:])