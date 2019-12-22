"""
Model of orders
"""

from dataclasses import dataclass

import typing


@dataclass(frozen=True)
class BuyMarketOrder:
    volume: int


@dataclass(frozen=True)
class SellMarketOrder:
    volume: int


@dataclass(frozen=True)
class BuyLimitOrder:
    volume: int
    limitprice: int


@dataclass(frozen=True)
class SellLimitOrder:
    volume: int
    limitprice: int


@dataclass(frozen=True)
class SellStopOrder:
    volume: int
    stopprice: int


@dataclass(frozen=True)
class BuyStopOrder:
    volume: int
    stopprice: int


OrderT = typing.Union[BuyMarketOrder, SellMarketOrder, BuyLimitOrder, SellLimitOrder, BuyStopOrder, SellStopOrder]
