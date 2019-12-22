"""Model for a wallet"""
from dataclasses import dataclass
from decimal import Decimal

import dpcontracts

from currency.currency import Currency
from currency.price import Price


@dataclass
class Wallet:
    amount: Decimal
    currency: Currency

    @dpcontracts.require("`price` must be a Price", lambda args: isinstance(args.price, Price))
    @dpcontracts.require("`price.currency` must be the same as the Wallet's currency", lambda args: args.self.currency == args.price.currency)
    def __sub__(self, price: Price):
        with self.currency.context() as ctx:
            return Wallet(amount=self.amount - price.total_price, currency=self.currency)



