"""
Model a currency
"""
from __future__ import annotations

import decimal
from dataclasses import dataclass, field

import dpcontracts

from currency.assetcontext import AssetContext


@dataclass(frozen=True, )
class Asset:
    uid: str  # TODO : improve ? guarantee unicity ?
    context: AssetContext = field(default_factory=AssetContext)

    @dpcontracts.require("`other` must be an Asset", lambda args: isinstance(args.other, Asset))
    @dpcontracts.require("`other` must be the same Asset as self", lambda args: args.other.uid == args.self.uid)
    def __add__(self, other: Asset):
        return self

    @dpcontracts.require("`other` must be an Asset", lambda args: isinstance(args.other, Asset))
    @dpcontracts.require("`other` must be the same Asset as self", lambda args: args.other.uid == args.self.uid)
    def __sub__(self, other: Asset):
        return self


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