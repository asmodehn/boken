from dataclasses import dataclass

from currency.assetvolume import AssetVolume
from currency.unitprice import UnitPrice


@dataclass
class TotalPrice:
    asset_volume: AssetVolume
    unit_price: UnitPrice

    def context(self):
        return self.unit_price.currency.context()

    def __call__(self, *args, **kwargs):
        """paying the price"""


