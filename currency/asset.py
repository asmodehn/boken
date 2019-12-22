"""
Model a currency
"""
from __future__ import annotations

import decimal
from dataclasses import dataclass, field

import dpcontracts
import typing
import weakref
from currency.assetcontext import AssetContext



@dataclass(frozen=True, init=False)
class Asset:
    instance_dict: typing.ClassVar[typing.Dict[str, Asset]] = dict()

    uid: str  # TODO : improve ? guarantee unicity ?
    context: AssetContext = field(default_factory=AssetContext)

    def __init__(self, uid: str, context: AssetContext = None):
        object.__setattr__(self, 'context', context if context is not None else AssetContext())
        object.__setattr__(self, 'uid', uid)
        self.instance_dict[uid] = self

    @dpcontracts.require("`other` must be an Asset", lambda args: isinstance(args.other, Asset))
    @dpcontracts.require("`other` must be the same Asset as self", lambda args: args.other.uid == args.self.uid)
    def __add__(self, other: Asset):
        return self

    @dpcontracts.require("`other` must be an Asset", lambda args: isinstance(args.other, Asset))
    @dpcontracts.require("`other` must be the same Asset as self", lambda args: args.other.uid == args.self.uid)
    def __sub__(self, other: Asset):
        return self

    def __call__(self, num: str = '0'):
        return self.context.create_decimal(num)


models = weakref.WeakValueDictionary()

@dpcontracts.require("`uid` must be unique, and not be present in models",
                     lambda args: args.uid not in models)
def model(uid, context: AssetContext = None):
    a = Asset(uid=uid, context=context)
    models[uid] = a
    return a



if __name__ == '__main__':

    a = Asset(uid="ThisGOOD")
    aa = Asset(uid="ThisGOOD")
    b = Asset(uid="ThisNOTthatGOOD")

    assert a == aa
    assert a != b
    assert b != aa

    # commutativity, monadic (transitivity, associativity trivial ?)
    assert a + aa == a == aa == aa + a

    # different context means different asset !
    aa1 = Asset(uid="ThisGOOD")

    assert a == aa1

    aa1.context.clamp = 1

    assert a != aa1
