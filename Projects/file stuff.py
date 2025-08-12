import os
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from colorama import Fore, Back, Style
import time
import hashlib


def checkIt(url):

        req = Request(url)
        response = urlopen(req)
        return 0




urls = open("C:\\Users\\jritter\\Desktop\\url.txt", "r")

for url in urls:
    start = time.time()
    url = url.strip()
    urlHash = "url" + str(int(hashlib.sha1(url.encode("utf-8")).hexdigest(), 16) % (10 ** 8)) + ".url"
    print(urlHash)
    result = checkIt(url)
    finish = time.time()
    total = round(finish - start, 3)

    if result == 0:
        if total <= .5:
            print(Fore.GREEN + f"{url} Fast: {total} seconds")
        if total > .5:
            print(Fore.YELLOW + f"{url} Slow: {total} seconds")
    elif result == 1:
        print(Fore.RED + f"{url} SITE DOWN")

    elif result == 2:
        print(Fore.RED + f"{url} Page Not Found")


