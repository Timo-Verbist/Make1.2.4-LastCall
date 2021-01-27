#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

import socket


def main():
    try:
        host_name = socket.gethostname()
        ip = socket.gethostbyname_ex(host_name)
        print("host name = " + host_name)
        print("ip LAN = ", end="")
        print(ip[2][0])
        print("ip WAN = ", end="")
        print(ip[2][1])
    except:
        print("\nSomething went wrong with\ngetting the host name and/or the ip")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
