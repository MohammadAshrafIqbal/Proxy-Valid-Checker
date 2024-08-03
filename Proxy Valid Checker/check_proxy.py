import threading
import queue
import requests

# Initialize a queue and a list for valid proxies
proxy_queue = queue.Queue()
working_proxies = []

# Read proxies from a file and load them into the queue
with open("proxy_list.txt", "r") as file:
    proxy_list = file.read().strip().split("\n")
    for proxy in proxy_list:
        proxy_queue.put(proxy)

# Function to test if proxies are valid
def test_proxy():
    global proxy_queue
    while not proxy_queue.empty():
        current_proxy = proxy_queue.get()
        try:
            response = requests.get("http://ipinfo.io/json", proxies={"http": current_proxy, "https": current_proxy}, timeout=10)
            if response.status_code == 200:
                working_proxies.append(current_proxy)
                print("Valid proxy found:", current_proxy)
        except Exception as err:
            print("Issue with proxy:", current_proxy, err)

# Create a list to hold thread references
threads = []
for _ in range(20):  # Number of concurrent threads can be adjusted
    thread = threading.Thread(target=test_proxy)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Proxy check complete.")
print("Valid proxies:", working_proxies)
