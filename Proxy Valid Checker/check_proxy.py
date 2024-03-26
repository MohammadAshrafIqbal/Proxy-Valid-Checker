import threading
import queue
import requests

#This code write by Mohammad Ashraf Iqbal (https://github.com/MohammadAshrafIqbal)

q = queue.Queue()
valid_proxies = []

# Load proxies from file into queue
with open("proxy_list.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

# Function to check proxies
def check_proxy():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("http://ipinfo.io/json", proxies={"http": proxy, "https": proxy}, timeout=10)
            if res.status_code == 200:
                valid_proxies.append(proxy)
                print("Valid proxy:", proxy)
        except Exception as e:
            print("Error with proxy:", proxy, e)

# Create threads to check proxies
threads = []
for _ in range(20):  # You can adjust the number of threads based on your requirement
    t = threading.Thread(target=check_proxy)
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

print("All proxies checked.")
print("Valid proxies:", valid_proxies)
