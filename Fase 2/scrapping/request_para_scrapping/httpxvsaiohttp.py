import asyncio
import time
import httpx
import aiohttp

'''
 
Comparação de desempenho entre HTTPX e AIOHTTP para requisições assíncronas
A aiohttp está mais lenta que a httpx para poucas requisições, mas para muitas requisições (1000) a aiohttp fica mais rápida. Além disso o httpx começou a da erros quando enviava muitas requisições (1000).
'''

async def main():
    # cria os clientes HTTPX e AIOHTTP
    httpx_client = httpx.AsyncClient()
    aiohttp_client = aiohttp.ClientSession()

    try:
        # Envia 100 requisições GET assíncronas usando HTTPX
        start_time = time.perf_counter()
        tasks = [httpx_client.get("https://example.com") for _ in range(100)]
        await asyncio.gather(*tasks)
        end_time = time.perf_counter()
        print(f"HTTPX: {end_time - start_time:.2f} seconds")      

        # Envia 100 requisições GET assíncronas usando AIOHTTP
        '''start_time = time.perf_counter()
        tasks = [aiohttp_client.get("https://example.com") for _ in range(1000)]
        await asyncio.gather(*tasks)
        end_time = time.perf_counter()
        print(f"AIOHTTP: {end_time - start_time:.2f} seconds")'''
    finally:
        # Fecha os clientes
        await aiohttp_client.close()
        await httpx_client.aclose()

asyncio.run(main())