import unittest
from parameterized import parameterized
import json
import marshmallow
from boken.ws import schemas
from boken.errors import BokenException

from boken.ws.heartbeat import Heartbeat
from boken.ws.pingpong import Ping, Pong
"""
Test module.
This is intended for extensive testing, using parameterized, hypothesis or similar generation methods
For simple usecase examples, we should rely on doctests.
"""

class TestHeartbeatSchema(unittest.TestCase):

    def setUp(self) -> None:
        self.schema = schemas.HeartbeatSchema()

    @parameterized.expand([
        # we make sure we are using a proper json string
        [json.dumps({"event": "heartbeat"})],
    ])
    def test_load_ok(self, payload):
        """ Verifying that expected data parses properly """
        parsed = self.schema.loads(payload)
        assert isinstance(parsed, Heartbeat)

    @parameterized.expand([
        # we make sure we are using a proper json string
        [json.dumps({"what": "isit"})],
        [json.dumps({"event": 42})],
        [json.dumps({"event": "some_other_string"})],
    ])
    def test_load_fail(self, payload):
        """ Verifying that unexpected data fails properly """
        with self.assertRaises(marshmallow.exceptions.ValidationError):
            self.schema.loads(payload)





class TestPingSchema(unittest.TestCase):

    def setUp(self) -> None:
        self.schema = schemas.PingSchema()

    @parameterized.expand([
        # we make sure we are using a proper json string
        [json.dumps({"event": "ping"})],
    ])
    def test_load_ok(self, payload):
        """ Verifying that expected data parses properly """
        parsed = self.schema.loads(payload)
        assert isinstance(parsed, Ping)

    @parameterized.expand([
        # we make sure we are using a proper json string
        [json.dumps({"what": "isit"})],
        [json.dumps({"event": 42})],
        [json.dumps({"event": "some_other_string"})],
    ])
    def test_load_fail(self, payload):
        """ Verifying that unexpected data fails properly """
        with self.assertRaises(marshmallow.exceptions.ValidationError):
            self.schema.loads(payload)

# TODO : fix this : one is load the other is dump...

class TestPongSchema(unittest.TestCase):

    def setUp(self) -> None:
        self.schema = schemas.PongSchema()

    @parameterized.expand([
        # we make sure we are using a proper json string
        [json.dumps({"event": "pong"})],
    ])
    def test_load_ok(self, payload):
        """ Verifying that expected data parses properly """
        parsed = self.schema.loads(payload)
        assert isinstance(parsed, Pong)

    @parameterized.expand([
        # we make sure we are using a proper json string
        [json.dumps({"what": "isit"})],
        [json.dumps({"event": 42})],
        [json.dumps({"event": "some_other_string"})],
    ])
    def test_load_fail(self, payload):
        """ Verifying that unexpected data fails properly """
        with self.assertRaises(marshmallow.exceptions.ValidationError):
            self.schema.loads(payload)


if __name__ == "__main__":
    unittest.main()
