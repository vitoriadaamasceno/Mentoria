import math

async def repeat_lyrics():
    await print_lyrics()
    await print_lyrics()

async def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

# Criar uma função assíncrona para envolver a chamada de repeat_lyrics()
async def main():
    await repeat_lyrics()

# Executar o loop de evento asyncio
import asyncio
asyncio.run(main())
