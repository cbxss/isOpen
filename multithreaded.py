import time
import requests
from threading import Thread
import random

college = "MAE"
courses = ["452", "440", "453", "451"]
hook = ''
cookie = ''


def request(course):
    print("Request " + course)
    url = "https://csulb.collegescheduler.com/api/terms/Fall%202021/subjects/" + college + "/courses/" + course + "/regblocks"
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


def checker(course):
    params = {
        'username': "zazoo",
        'content': college + " " + course + " COURSE AVAILABLE"
    }
    has_class = request(course)
    print(has_class)
    while True:
        has_class = request(course)
        if has_class:
            requests.post(hook, params)
            time.sleep(500 + (random.randint(0, 500)))  # 10ish minutes
        else:
            time.sleep(500 + (random.randint(0, 500)))  # 10ish minutes


def main():
    for i in courses:
        Thread(target=checker, args=(i,)).start()


if __name__ == "__main__":
    main()
