from colorama import Fore, Back, Style
from mac_changer import *
from scanning import *
from sqli_scan import *
from dir_scan import *
from xss_detector import *
banner = """
.___          _____ .__         .__   __           
|   |  ____ _/ ____\|__|  ____  |__|_/  |_  ___.__.
|   | /    \\   __\ |  | /    \ |  |\   __\<   |  |
|   ||   |  \|  |   |  ||   |  \|  | |  |   \___  |
|___||___|  /|__|   |__||___|  /|__| |__|   / ____|
          \/                 \/             \/     

First time huh? Enter "help" to get more infomation :) \nHappy Hacking !!"""
print(Fore.CYAN + banner)
def main():
    while True:
        command = input("\nEnter command here -> ")
        if command == "help":
            menu = """        1. Scanning options for specific host
        2. Change Media Access Control address (Linux Only)
        3. Directory Scanning
        4. XSS Detector
        
Enter "q" to exit !
        """
            print(menu)
        elif command == '1':
            scan()
        elif command == '2':
            mac_changer_main()
        elif command == '3':
            dir_scan()
        elif command == '4':
            target = input("[+] Enter target to scan for XSS: ")
            scan_xss(target)
        elif command == 'q':
            print("Bye :))")
            break
            sys.exit(0)

if __name__ == "__main__":
    main()