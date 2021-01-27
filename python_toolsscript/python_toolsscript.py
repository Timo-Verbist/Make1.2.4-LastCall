#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

from scripts import IP_display, passwordgenerator, system_update_and_upgrade, software_installation, systeminfo, networkscanner, gpio_pin_and_state, calculator


def main():
    while True:
        print("Main menu:")
        print("1: IP display                    6: network and/or portscanner")
        print("2: Passwordgen                   7: display gpio pin + state")
        print("3: system update -and grade      8: calculator")  # self chosen function
        print("4: Software installation         9: quit")
        print("5: display system info")

        try:
            choice = int(input("Give your choice\n"))
        except:
            print("invalid input!\n")
            main()

        if choice == 1:
            IP_display.main()
        elif choice == 2:
            passwordgenerator.main()
        elif choice == 3:
            system_update_and_upgrade.main()
        elif choice == 4:
            software_installation.main()
        elif choice == 5:
            systeminfo.main()
        elif choice == 6:
            networkscanner.main()
        elif choice == 7:
            gpio_pin_and_state.main()
        elif choice == 8:
            calculator.main()
        elif choice == 9:
            quit()
        else:
            print("This choice does not apply")
        print("\n")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
