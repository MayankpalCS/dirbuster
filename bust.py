import requests
import queue
import threading
import sys

host = sys.argv[1]
threads = int(sys.argv[2])

try:
    requests.get(host)
except Exception as e:
    print('Host resolution error')
    exit()
wordlist=open('directorybust.txt', 'r')
q = queue.Queue()


def busting(thread, q):
    while True:
        url = q.get()

        response = requests.get(url,allow_redirects=False)
        if response.status_code == 200:
            print(f"[+]{url} directory exists")
        q.task_done()
for words in wordlist.read().splitlines():

    url = host + '/' + words
    q.put(url)
for i in range(threads):
    t = threading.Thread(target=busting,args=(i,q))
    t.daemon = True
    t.start()




