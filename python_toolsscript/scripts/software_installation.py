#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

import os


def main():
    software = str(input("What software do you want to install?\n"))
    command = "sudo apt-get install " + software
    os.system(command)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
