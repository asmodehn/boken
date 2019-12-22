"""
Model of a Price
"""
from dataclasses import dataclass
from decimal import Decimal

import dpcontracts

from currency.asset import Currency, AssetVolume



@dataclass
class UnitPrice:

    price: Decimal
    currency: Currency

    @dpcontracts.require("`avolume` must be an AssetVolume", lambda args: isinstance(args.avolume, AssetVolume))
    @dpcontracts.require("`avolume.asset` must be different from currency", lambda args: args.avolume.asset != args.self.currency)
    def __mul__(self, avolume: AssetVolume):

        with self.currency.context() as ctx:
            return TotalPrice(asset_volume=avolume, unit_price=self)



