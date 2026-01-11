import requests
import time

def fetch_url(url):
    """Sends a GET request and waits for the response."""
    try:
        # EXECUTION BLOCKS HERE: The program pauses until the server responds
        response = requests.get(url, timeout=10)
        print(f"Completed: {url}, Status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Failed: {url}, Error: {e}")

# A list of 15 URLs to scrape
urls = [
    "https://www.lipsum.com/",
    "http://automationpractice.com/",
    "https://demo.automationtesting.in/Register.html"
] * 5

print("Starting synchronous scrape...")
start_time = time.time()

# Loop throguh all the URLs in the list
for url in urls:
    fetch_url(url)

duration = time.time() - start_time
print(f"\nFinished. Total time: {duration:.2f} seconds.")