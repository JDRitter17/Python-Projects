from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from colorama import Fore, Style
import time
import hashlib
import os

def get_filename(url):
    """Generate a consistent filename from URL hash"""
    return "data" + str(int(hashlib.sha1(url.encode("utf-8")).hexdigest(), 16) % (10 ** 8)) + ".data"

def checkForChanges(url):
    fileName = get_filename(url)

    if not os.path.exists(fileName):
        open(fileName, "x").close()

    with open(fileName, "rb") as file:
        savedData = file.read()

    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    response = urlopen(req)
    newData = response.read()

    if savedData == newData:
        return "Same"
    else:
        with open(fileName, "wb") as file:
            file.write(newData)
        return "Diff"

def checkIt(url):
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        response = urlopen(req)
        return 0  # Up
    except HTTPError as e:
        if e.code == 404:
            return 1  # 404 error
        else:
            return 3  # Other HTTP errors
    except URLError:
        return 2  # Down / unreachable

print(f"{'Stat':<8}{'Time':<8}{'Changed':<14}URL")
print("-" * 42)

try:
    with open(r"C:\Users\jritter\Desktop\url.txt", "r") as urls:
        for url in urls:
            url = url.strip()
            start = time.time()
            result = checkIt(url)
            finish = time.time()
            total = finish - start

            if result == 0:
                change = checkForChanges(url)
                color = Fore.GREEN if total <= 0.3 else Fore.YELLOW
                print(f"{color}Up      {total:.3f}s  {change:<10} {url}{Style.RESET_ALL}")

            elif result == 1:
                print(f"{Fore.RED}404      {'':<14} {url}{Style.RESET_ALL}")

            elif result == 2:
                print(f"{Fore.RED}Down     {'':<14} {url}{Style.RESET_ALL}")

            elif result == 3:
                print(f"{Fore.RED}Error    {'':<14} {url}{Style.RESET_ALL}")

except KeyboardInterrupt:
    print("\nProcess interrupted by user. Exiting.")
