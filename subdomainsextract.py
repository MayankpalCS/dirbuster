import time

import requests
import queue
import threading
import sys
import argparse
from colorama import init, Fore

init()
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
reset = Fore.RESET
def banner():
    print(f"""{green}
           |------|  ------- |-----|     |-----| |     | |--------| -------- |----- |----|
           |      |     |    |     |     |     | |     | |             |     |      |    |
           |      |     |    |-----|     |-----| |     | |-------|     |     |----- |----|
           |      |     |    ||          |     | |     |         |     |     |      ||
           |------|  ------- |  |        |-----| |-----| |-------|     |     |----- | |
            @ developed by mayank |                                                     |
                           """)


banner()

argparse = argparse.ArgumentParser(description="Use this tool to bust directories",
                                   usage="python3" + sys.argv[0] + "-u [domain] -t [no_of+threads] -d subdomainwordlist.txt ")
argparse.add_argument("-u", "--url", help="Enter the url name on which you want to perform directory busting",
                      required=True)
argparse.add_argument("-t", "--threads", help="no of threads", required=True)
argparse.add_argument("-d", "--direc", help="Enter the name of wordlist one is provided,Fell free to name that",
                      required=True)
args = argparse.parse_args()  # parsed the values
host = args.url  # above we enteres --domain will be fetched hhere
threads = int(args.threads)
wordlist = args.direc
q = queue.Queue()

wordlist = open(wordlist, 'r')
for words in wordlist.read().splitlines():
    url = 'https://' + words + '.' + host
    q.put(url)


def sub_find(thread, q):
    while True:
        url = q.get()
        try:
            res = requests.get(url, allow_redirects=False,timeout=2)
            if res.status_code != 404:
                print(f"{green}[+]{url} is there")
        except Exception as e:
            print(f"{red}-----------------press ctrl+c if no response-----------------")
        q.task_done()


for i in range(threads):

    time.sleep(1)
    t = threading.Thread(target=sub_find, args=(i, q))
    t.daemon = True
    t.start()
