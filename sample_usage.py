import signal
import random
import numpy as np
import asyncio


EXCHANGE_HISTORY_SIZE=7
QUEUE_BUFFER_SIZE=3

Q = asyncio.queues.Queue(maxsize=QUEUE_BUFFER_SIZE)

# random walk as function of one value
def walk_next(x):
    step_x = random.randint(0, 1)
    if step_x == 1:
        return x + 1 + np.random.normal()
    else:
        return x - 1 + np.random.normal()


#  as generator to return a sliding window and an extra value
def random_walk(xs):
    for x in xs[-EXCHANGE_HISTORY_SIZE:]:
        yield x
    yield walk_next(xs[-1])


# with random progress as coroutine
async def random_progress(xs):
    await asyncio.sleep(1 + np.random.normal())
    s = ""
    for x in random_walk(xs):
        s = s + f" {x} "
    print('X: ' + s)
    # append last element (that was generated)
    xs.append(x)
    return xs


# as a dummy exchange implementation
async def exchange(x = None, loop = None):
    loop = loop or asyncio.get_event_loop()
    x = x or [0]

    nx = await random_progress(x)

    # enqueueing
    try:
        Q.put_nowait(nx[-1])
    except asyncio.queues.QueueFull:
        Q.get_nowait()  # dropping early message
        Q.put_nowait(nx[-1])

    # reschedule itself
    loop.create_task(exchange(nx, loop))

# for design help
# TODO : remove previous code and replace with boken, once it is usable

# Local (async / websocket) Client for this locally simulated exchange :
# Note: we do NOT concern ourselves with a  usual rest/sync client.


# TODO : find some kind of symmetry here to guide design...
async def client(vs = None, loop=None):
    loop = loop or asyncio.get_event_loop()

    vs = vs or [0]
    # blocking get

    v = await Q.get()
    vs.append(v)

    s = ""
    for v in vs:
        s = s + f" {v} "
    print('C: ' + s)

    # reschedule itself
    loop.create_task(client(vs, loop))











@asyncio.coroutine
def ask_exit(sig_name):
    print("got signal %s: exit" % sig_name)
    yield from asyncio.sleep(2.0)
    asyncio.get_event_loop().stop()

loop = asyncio.get_event_loop()

loop.create_task(exchange())
loop.create_task(client())

for signame in ('SIGINT', 'SIGTERM'):
    loop.add_signal_handler(
        getattr(signal, signame),
        lambda: asyncio.ensure_future(ask_exit(signame))
    )
loop.run_forever()
