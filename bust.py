import requests
import queue
import threading

f=open("123456.txt","r")
threads=int(input("Enter number of threads"))
wordlist=input("Enter the name of wordlist file.")
dom=input("Enter url")
a="pdisaf"
q=queue.Queue()
def banner():
    print("""
           |------|  ------- |-----|     |-----| |     | |--------| -------- |----- |----|
           |      |     |    |     |     |     | |     | |             |     |      |    |
           |      |     |    |-----|     |-----| |     | |-------|     |     |----- |----|
           |      |     |    ||          |     | |     |         |     |     |      ||
           |------|  ------- |  |        |-----| |-----| |-------|     |     |----- | |
            @ developed by mayank |                                                     |
                           """)
banner()
try:
    requests.get(f"https://{dom}")
except Exception as e:
    print(f'Host resolution error')
    exit()

for line in f:
    word=line.split()
    url=f"https://{str(dom)}/{str(word[0])}"
    q.put(url)


def target():
    while not q.empty():
        url=q.get()
        response=requests.get(url)
        if response.status_code !=404:
            print({url})

for i in range(threads):
    t=threading.Thread(target=target)
    t.start()
