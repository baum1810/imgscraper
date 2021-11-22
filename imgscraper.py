import requests, random
from os import system
import threading
from dhooks import Webhook

hook = Webhook('YOUR WEBHOOK')
threads = 300

def scrape():
    while True:
        Ran = ''.join(random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcbnm123456789') for i in range(7))
        link = f"https://i.imgur.com/{Ran}.png"
        img = requests.get(link, allow_redirects=True)
        if img.url == "https://i.imgur.com/removed.png":
            pass
        else:
            hook.send(link)

for i in range(threads):
    t = threading.Thread(target=scrape)
    t.start()




