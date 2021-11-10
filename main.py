import random
import time
import requests

college = "CECS"
course = "100"
hook = '' #discord webhook
cookie = '' #csulb cookie
year = '2022'

#Change to Spring or Fall accordingly 
url = "https://csulb.collegescheduler.com/api/terms/Spring%20"+year+"/subjects/" + college + "/courses/" + course + "/regblocks"


def request():
    payload = {}
    headers = {
        'authority': 'csulb.collegescheduler.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'accept': '*/*',
        'sec-gpc': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie
    }
    print(requests.request("GET", url, headers=headers, data=payload).text)
    return requests.request("GET", url, headers=headers, data=payload).json()["registrationBlocks"][0]["enabled"]


params = {
    'username': "zazoo",
    'content': college + " " + course + " COURSE AVAILABLE"
}

has_class = request()
print(has_class)
while True:
    has_class = request()
    if has_class:
        requests.post(hook, params)
        time.sleep(500 + (random.randint(0, 500)))  # 15 minutes
    else:
        time.sleep(500 + (random.randint(0, 500)))
