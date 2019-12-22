import typing
from dataclasses import dataclass

from currency.currency import Currency
from currency.price import Price
from currency.wallet import Wallet


@dataclass
class Agent:
    wallets: typing.Dict[Currency, Wallet]

    def __call__(self, price: Price):
