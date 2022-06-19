import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

def get_all_forms(url): # Get all forms tag in html page
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form): # Get attributes details of forms tag
    details = {}
    inputs = []

    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})

    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value): # Send request with specific data
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def scan_xss(url): # Scan for xss vulnerable, check response content to detect it
    forms = get_all_forms(url)
    print("[+] Detected " + str(len(forms)) + " forms on " + url)
    js_script = "<Script>alert('hi')</scripT>"
    if len(forms) == 0:
        print("[X] Error ! There are no forms on this page !")
    else:
        for form in forms:
            form_details = get_form_details(form)
            content = submit_form(form_details, url, js_script).content.decode()
            if js_script in content:
                print("[+] Using payload: " + js_script)
                print("\n[✅] Payload found on resonse content \n=> This website maybe have XSS !!")
            else:
                print("[X] This website maybe have no XSS vulnerable !!")
# target = "https://cystack.net/"
# scan_xss(target)