import aiohttp
import asyncio
import time


async def get_sites(link):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as response:
                print(f"Completed request from {link} and status {response.status}")

    except aiohttp.ClientError as e:
        print(f"Failed request from {link} error {e}")

links = [
    "https://www.lipsum.com/",
    "http://automationpractice.com/",
    "https://demo.automationtesting.in/Register.html"
] * 5

print("Starting async scrape...")
start_time = time.time()

# Loop throguh all the URLs in the list
for link in links:
    asyncio.run(get_sites(link))

duration = time.time() - start_time
print(f"\nFinished. Total time: {duration:.2f} seconds.")