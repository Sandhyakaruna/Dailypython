import threading
import requests
from time import time

# Define a function to download a web page
def download_page(url):
    response = requests.get(url)
    print(f"Downloaded {url}, status code: {response.status_code}")


urls = ["(link unavailable)", "(link unavailable)", "(link unavailable)"]


threads = []
start_time = time()
for url in urls:
    thread = threading.Thread(target=download_page, args=(url,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(f"Total time taken: {time() - start_time} seconds")
