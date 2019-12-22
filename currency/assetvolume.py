from __future__ import annotations

import decimal
from dataclasses import dataclass

import dpcontracts

from currency.asset import Asset
from currency.totalprice import TotalPrice
from currency.unitprice import UnitPrice


@dataclass
class AssetVolume:
    volume: decimal.Decimal
    asset: Asset

    @dpcontracts.require("`uprice` must be a UnitPrice", lambda args: isinstance(args.uprice, UnitPrice))
    @dpcontracts.require("`uprice` currency must not be the asset", lambda args: args.self.asset != args.uprice.currency)
    def __mul__(self, uprice: UnitPrice):
        # should we be in price context or in asset context ???
        with uprice.currency.context() as ctx:
            return TotalPrice(asset_volume=self, unit_price=uprice)

    @dpcontracts.require("`other` must be an AssetVolume", lambda args: isinstance(args.other, Asset))
    @dpcontracts.require("`other` asset must be the same Asset as self", lambda args: args.other.asset == args.self.asset)
    def __add__(self, other: AssetVolume):
        with self.asset.context() as ctx:
            return AssetVolume(volume= self.volume + other.volume, asset=self.asset)

    @dpcontracts.require("`other` must be an Asset", lambda args: isinstance(args.other, Asset))
    @dpcontracts.require("`other` must be the same Asset as self", lambda args: args.other.uid == args.self.uid)
    def __sub__(self, other: AssetVolume):
        return self
