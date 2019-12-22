"""
Model of an account : a client of the exchange
"""
import typing
from dataclasses import dataclass

from boken.exchange.balance import Balance
from boken.exchange.order import OrderT


@dataclass
class Account:

    balance: Balance  # TMP currently only one market
    orders: typing.List[OrderT]
