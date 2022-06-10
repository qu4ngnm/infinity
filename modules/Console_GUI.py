from colorama import Fore, Back, Style

def console_gui():
    banner = """
.___          _____ .__         .__   __           
|   |  ____ _/ ____\|__|  ____  |__|_/  |_  ___.__.
|   | /    \\   __\ |  | /    \ |  |\   __\<   |  |
|   ||   |  \|  |   |  ||   |  \|  | |  |   \___  |
|___||___|  /|__|   |__||___|  /|__| |__|   / ____|
          \/                 \/             \/     
          
First time huh? Enter "help" to get more infomation :) \nHappy Hacking !!"""
    print(Fore.CYAN + banner)
    command = input("\nEnter command here -> ")
    if command == "help":
        menu = """    1. Scanning options for specific host
    2. Bruteforce something (ssh,...)
    3. Change Media Access Control address (Linux Only)
    4. Directory Scanning
    5. SQL Injection Detector"""
        print(menu)