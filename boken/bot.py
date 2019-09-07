import asyncio

import time

from aiokraken.rest import RestClient, Server

# TOOD : Eventually the Bot should be a (set of) proactors & reactors...
async def ohlc(client):

    await asyncio.sleep(10.0)
    modeldf = await client.ohlc('ETHEUR')
    print(modeldf.head())
    asyncio.create_task(ohlc(client))




if __name__ == '__main__':

    client = RestClient(Server())
    loop = asyncio.get_event_loop()

    loop.create_task(ohlc(client))

    loop.run_forever()





