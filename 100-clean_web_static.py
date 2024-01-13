#!/usr/bin/python3
"""
Defines function that cleans the websever of outdated archives.
Author: Pius Aaron
Date: 13-01-2024
Time: 22:33
"""

import os
from fabric.api import run, local, env
from datetime import datetime

env.hosts = ['18.234.253.75', '54.174.123.116']


def do_clean(number=0):
    """
    Removes archives from the versions directory from the local machine
    and from /data/web_static/releases/ directory

    Usage: do_clean(2)
        -> leaves only two most recent archives

    Arguments:
                number: int -> number of archives to keep

    keeps only the latest archive when number == 0 or number == 1
    """

    number = int(number)
    # Gets list of archives
    local_archives = local('ls versions', capture=True).split()

    # Gets the dates of the archives from their names for sorting
    # before deleting
    dates = sorted([datetime.strptime(x[10:-4], '%Y%m%d%H%M%S')
                   for x in local_archives])
    dates = [date.strftime('%Y%m%d%H%M%S') for date in dates]

    # determines the number of archives to reserve
    if number in (1, 0):
        num_of_arch_del = len(local_archives) - 1
    else:
        num_of_arch_del = len(local_archives) - number

    dates = dates[:num_of_arch_del]

    # deletes the archives
    for date in dates:
        for arch in local_archives:
            if date in arch:
                local('rm versions/{}'.format(arch))
                run('rm /data/web_static/releases/{}'.format(arch))
