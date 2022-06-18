import sys
import subprocess
import random
import re

def change_mac(interface, new_mac_address): # This function to change mac on Linux with command
    subprocess.call(["sudo", "ifconfig", interface, b"down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def get_random_mac_address(): # This function to get random mac address
    characters = "0123456789abcdef"
    random_mac_address = "00"
    for i in range(5):
        random_mac_address += ":" + random.choice(characters) + random.choice(characters)
    return random_mac_address

def get_current_mac(interface):  #  Function get current mac address
    output = subprocess.check_output(["ifconfig", interface])
    return re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output)).group(0) # using regular expression to get exact current mac address

def mac_changer_main(): # Here is main function
    interface = input("[+] Enter network interface: ")
    mode = input("[+] Press 1 to auto change MAC\n[+] Press 2 to change MAC mannually !\n=> ")
    current_mac = get_current_mac(interface)
    try:
        if(int(mode) == 1):
            random_mac = get_random_mac_address()
            change_mac(interface, random_mac)
            new_mac_summary = subprocess.check_output(
                ["ifconfig", interface])
            if random_mac in str(new_mac_summary):
                print("\r[*] MAC Address Changed to", random_mac,end=" ")
                sys.stdout.flush()
            else:
                print("\r[*] MAC Address Changed Failed !!")
                sys.stdout.flush()
        elif(int(mode) == 2):
            mannually_mac = input("[+] Enter new MAC address: ")
            change_mac(interface, mannually_mac)
            new_mac_summary = subprocess.check_output(
                ["ifconfig", interface])
            if mannually_mac in str(new_mac_summary):
                print("\r[*] MAC Address Changed to", mannually_mac, end=" ")
                sys.stdout.flush()
            else:
                print("\r[*] MAC Address Changed Failed !!", mannually_mac, end=" ")
                sys.stdout.flush()
    except KeyboardInterrupt:
        change_mac(interface, current_mac)
        print("\n[+] Quitting Program...")