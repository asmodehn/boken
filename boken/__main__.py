import asyncio

from boken.aio import kraken


async def get_time():
    print("Getting Kraken time`")
    response = await kraken.get_time()
    print(response)
    return response


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_time())
