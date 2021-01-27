#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

import os


def main():
    os.system("lscpu")  # systeminfo in windows


if __name__ == '__main__':  # code to execute if called from command-line
    main()
