import requests
import queue
import threading
import sys
import argparse
argparse=argparse.ArgumentParser(description="Use this tool to bust directories",usage="python3"+sys.argv[0]+"-u [url] -t [no_of+threads] -d directorybust.txt ")
argparse.add_argument("-u","--url",help="Enter the url name on which you want to perform directory busting",required=True)
argparse.add_argument("-t","--threads",help="no of threads",required=True)
argparse.add_argument("-d","--direc",help="Enter the name of wordlist one is provided,Fell free to name that",required=True)
args=argparse.parse_args()#parsed the values
host=args.url#above we enteres --domain will be fetched hhere
threads=int(args.threads)
wordlist=args.direc
try:
    requests.get(host)
except Exception as e:
    print('Host resolution error')
    exit()

wordlist=open(wordlist, 'r')
q = queue.Queue()


def busting(thread, q):
    while True:
        url = q.get()

        response = requests.get(url,allow_redirects=False)
        if response.status_code != 404:
            print(f"[+]{url} directory exists")
        q.task_done()
for words in wordlist.read().splitlines():

    url = host + '/' + words
    q.put(url)
for i in range(threads):
    t = threading.Thread(target=busting,args=(i,q))
    t.daemon = True
    t.start()




