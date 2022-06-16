import nmap

# tek4.vn 125.212.235.148

def scan():
    print("Infomation Gathering")
    host = input("[+] Enter host to scan <IP Type Only>: ")
    portScanner = nmap.PortScanner()
    result =  portScanner.scan(host, arguments="-T4 -sS -O -v")
    with open("../result/nmap_scan.json", "w+") as scanned_data:
        scanned_data.write(str(result))
    # print(result)
    for port in result['scan'][str(host)]["tcp"]:
        print("Port open and Services")
        print(str(port)  + ": " + result['scan'][str(host)]["tcp"][port]["name"] + " " + result['scan'][str(host)]["tcp"][port]["state"])
    print("\n\nOS Details")
    for os in result['scan'][str(host)]["osmatch"]:
        print(os["name"])
    print("""Open file "result/nmap_scan.json" for more infomation !!""")