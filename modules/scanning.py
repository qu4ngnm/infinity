import nmap

# tek4.vn 125.212.235.148

def scan():
    host = input("[+] Enter host to scan: ")
    portScanner = nmap.PortScanner()
    result =  portScanner.scan(host, arguments="-T4 -sS -O -v")
    for port in result['scan'][str(host)]["tcp"]:
        print("Port open and Services")
        print(str(port)  + ": " + result['scan'][str(host)]["tcp"][port]["name"] + " " + result['scan'][str(host)]["tcp"][port]["state"])
    print("\n\nOS Details")
    for os in result['scan'][str(host)]["osmatch"]:
        print(os["name"])
scan()