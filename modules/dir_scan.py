import requests

def req(url): # Request and return response status code
    try:
        return requests.get(url).status_code
    except requests.exceptions.ConnectionError:
        pass

def dir_scan(): # scan if status code is 200 then print it
    host = input("[+] Enter URL to scan: ")
    wordlist = open("../resources/wordlist_med.txt", 'r')
    for line in wordlist:
        word = line.strip()
        full_url = host + "/" + word
        response = req(full_url)
        if response == 200:
            results = "[✅] Found => " + full_url
            print(results)
