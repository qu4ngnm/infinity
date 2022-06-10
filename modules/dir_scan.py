import requests

def req(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass
def dir_scan():
    host = input("[+] Enter URL to scan: ")
    wordlist = open("../resources/wordlist_med.txt", 'r')
    for line in wordlist:
        word = line.strip()
        full_url = host + "/" + word
        response = req(full_url)
        if response != 200:
            print(full_url + "[✅] Found")