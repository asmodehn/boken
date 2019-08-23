import unittest
from parameterized import parameterized
import json
import marshmallow
from boken.ws import schemas
from boken.errors import BokenException

from boken.ws import msgq

"""
Stress test for our observable and controllable message queue
"""


class TestMessageQueue(unittest.TestCase):

    async def coro(self, data, **kwargs):
        return 42

    def setUp(self) -> None:
        self.mq = msgq.MessageQueue(name="testq", coro=self.coro, maxlen=1)

    @parameterized.expand([
        # we make sure we are using a proper json string
        ["some_random_message"],
    ])
    def test_normal_seq(self, msg):
        assert len(self.mq) == 0
        assert repr(self.mq) == f"{self.mq.name}:0/1"
        self.mq(msg)
        assert len(self.mq) == 1
        assert 42 == next(self.mq)

    def test_counter_seq(self, msg):
        assert len(self.mq) == 0
        with self.assertRaises(EmptyMessageQueue):
            next(self.mq)
        assert len(self.mq) == 0
        self.mq(msg)
        assert len(self.mq) == 1




def test_underflow_resilience():
    """ Testing behavior on underflow (not enough messages arriving in queue)"""
    pass


def test_overflow_resilience():
    """ Testing behavior on overflow (too many messages arriving in the queue)"""
    pass
