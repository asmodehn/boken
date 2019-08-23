import asyncio
import collections
import uplink
from dataclasses import dataclass

from .api import Kraken as APIKraken
from .ws import Kraken as WsKraken

api_kraken = APIKraken(base_url="https://api.kraken.com/", client=uplink.AiohttpClient())
ws_beta_kraken = WsKraken(base_url='wss://ws-sandbox.kraken.com/')
ws_kraken = WsKraken(base_url='wss://ws.kraken.com')



class ControlledQueue:
    """
    Currently a basic queue : https://github.com/python/cpython/blob/master/Lib/asyncio/queues.py
    But we should eventuallyimprove it with means of controlling overflow in a more fine grained manner than just blocking everything or not....

    We want to manage our message queues here, to avoid overflows.
    KISS but we need observability and controlability ! https://docs.honeycomb.io/learning-about-observability/intro-to-observability/
    """

    def __init__(self, name, coro, loop = None, maxsize=0):
        """
        Create a controlled queue
        :param name: an identifier for this queue, used only for observability purposes, and could be managed outside this class.
        :param coro: corountine to run when we want to process a message in the queue (will execute *sometime* between the append() and the pop() for that element)
        :param loop:
        :param maxsize: 0 means unbounded queues
        """
        self.loop = loop or asyncio.get_event_loop()
        self.name = name
        self.coro = coro
        self.queue = asyncio.Queue(maxsize=maxsize)

        # We need to have some looping function to empty the queue when it fills up too fast...
        #  Eventually we might need to drop messages, but *not silently* and we need one exception *aggregating multiple losses*...
        # TODO : some control theory here ? We should manage overflows somehow...

    def __call__(self, data, **kwargs):
        """
        Enqueues task, that will be run in the background.
        :param data: data to pass to the coro to make a task.

        :param kwargs: potential arguments to pass to the coro to modify behavior
        :return: the result of a previous task (FIFO)

        This may raise a QueueFull Exception
        """
        self.queue.put_nowait(asyncio.create_task(self.coro(data, **kwargs)))

    def __iter__(self):
        """Iterate on FIFO queue, poping messages out.
            Notice this is a generator only on task that finished already.
            get the result of the task. will block if the the queue is empty"""

        t = self.queue.get()  # waiting : this will block if queue is empty. If this is undesirable, uses the async interface.
        r = t.result()
        self.queue.task_done()
        yield r  # how to return ? OVERFLOW problem

    async def __aiter__(self):
        """get the result of the task asynchronously : will not 'block'."""
        t = await self.queue.get() # waiting. this is async : no problem
        r = await t.result()
        self.queue.task_done()
        yield r  # how to return ? OVERFLOW problem

    def __repr__(self):
        return f"{self.name}:{self.queue.qsize()/self.queue.maxsize}"

    def __len__(self):
        return self.queue.qsize()


    def __del__(self):
        """ Mandatory cleanup """
        await self.queue.join()
        # Cancel our worker tasks.
        for task in tasks:
            task.cancel()
        # Wait until all worker tasks are cancelled.
        await asyncio.gather(*tasks, return_exceptions=True)

def task_background(q):



def task_result(q):



async def task_result(q):
    t = q.get()  # wait or no_wait ? UNDERFLOW problem
    r = await t.result()
    q.task_done()
    yield r  # how to return ? OVERFLOW problem




class MessageQueue:
    """
    We want to manage our message queues here, to avoid overflows.
    KISS but we need observability and controlability ! https://docs.honeycomb.io/learning-about-observability/intro-to-observability/
    """

    def __init__(self, name, coro, loop = None, maxsize=512):
        self.loop = loop or asyncio.get_event_loop()
        self.name = name
        self.coro = coro
        self.queue = asyncio.Queue(maxsize=maxlen)

        # We need to have some looping function to empty the queue when it fills up too fast...
        #  Eventually we might need to drop messages, but *not silently* and we need one exception *aggregating multiple losses*...
        # TODO : some control theory here ? We should manage overflows somehow...

if __name__ == '__main__':
    # TODO : run doctests
    pass
    # TODO : also run an example loop to demonstrate control overtime...