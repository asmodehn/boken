import asyncio
import signal

from exchange import simexchange


@asyncio.coroutine
def ask_exit(sig_name):
    print("got signal %s: exit" % sig_name)
    yield from asyncio.sleep(2.0)
    asyncio.get_event_loop().stop()


loop = asyncio.get_event_loop()

# Running the exchange as standalone
loop.create_task( simexchange())


for signame in ('SIGINT', 'SIGTERM'):
    loop.add_signal_handler(
        getattr(signal, signame),
        lambda: asyncio.ensure_future(ask_exit(signame))
    )
loop.run_forever()