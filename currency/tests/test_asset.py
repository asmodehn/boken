import unittest

import dpcontracts
from hypothesis import given, infer

from currency.asset import Asset, model, models


class TestAsset(unittest.TestCase):
    @given(uid=infer)
    def test_model(self, uid: str):
        # artificially cleaning up models for test run
        models.clear()

        a = model(uid)

        with self.assertRaises(dpcontracts.PreconditionError) as exc_ctx:

            b = model(uid)

        assert exc_ctx

    @given(uid=infer)
    def test_init(self, uid: str):

        a = Asset(uid=uid)

        assert a.uid == uid

        # TODO : test context ??

    @given(uid=infer)
    def test_add(self, uid: str):
        a = Asset(uid=uid)

        assert a + a == a

        b = a

        assert a + b == b + a == a == b

    @given(uid=infer)
    def test_sub(self, uid: str):
        a = Asset(uid=uid)

        assert a - a == a

        b = a

        assert a - b == b - a == a == b

    @given(uid=infer)
    def test_call(self, uid: str):
        a = Asset(uid=uid)

        assert a("42") == a.context.create_decimal("42")


if __name__ == "__main__":
    unittest.main()
