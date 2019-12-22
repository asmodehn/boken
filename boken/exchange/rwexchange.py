"""
A model of an exchange, processing orders...
This exchange can run on its own for manual testing purposes (see __main__)
or can run as part of boken for simulation (potentially simultaneously to the actual implementation).
"""
import asyncio
import random

import typing

from boken.exchange.balance import Balance, Currency
from boken.exchange import order
from boken.exchange.order import OrderT

from boken.exchange.account import Account

class RWExchange:
    """ RAndom Walk Exchange"""

    def __init__(self, accounts: typing.Dict[typing.AnyStr,Account]):

        self.accounts = accounts

        # TMP : unique market for now...


        # Initialize ticker prices with dummy values
        self.ask_price = 100
        self.bid_price = 1

        # start looping immediately (first call has to be sync!)
        self()

    async def __call__(self, *args, **kwargs):
        """process a set of order"""

        # TMP : unique market for now...
        print(f"Bid: {self.bid_price} Ask: {self.ask_price}")

        for n, a in self.accounts.items():
            # process market orders first !
            market_orders = filter(lambda o: isinstance(o, BuyMarketOrder) or isinstance(o, SellMarketOrder), a.orders)

            for mo in market_orders:
                # this is a gross approximation but whatever works as a first implementation...

                if isinstance(mo, SellMarketOrder):
                    sold_amount = mo.volume
                    sold_price = self.bid_price
                    a.balance.base.amount += sold_price * sold_amount
                    a.balance.quote.amount -= sold_amount

                elif isinstance(mo, BuyMarketOrder):
                    bought_amount = mo.volume
                    bought_price = self.ask_price
                    a.balance.base.amount -= bought_price * bought_amount
                    a.balance.quote.amount += bought_amount

            # TODO : other orders


            # next check limit order, if limit reached -> market

            # next check stop order, if stop reached -> market


        # market evolution
        self.ask_price += random.randint(-(self.ask_price - self.bid_price)//2, 1)
        self.bid_price += random.randint(-(self.bid_price - 1), (self.ask_price - self.bid_price) // 2)

        await asyncio.sleep(.1)
        # loops
        asyncio.create_task(self(*args, **kwargs))


if __name__ == '__main__':

    import signal

    @asyncio.coroutine
    def ask_exit(sig_name):
        print("got signal %s: exit" % sig_name)
        yield from asyncio.sleep(2.0)
        asyncio.get_event_loop().stop()


    loop = asyncio.get_event_loop()

    # Running the exchange as standalone
    orders = []
    account = Account(balance=Balance(base=Currency(amount=100, name='EUR'), quote=Currency(amount=1, name='XCC')), orders=[])
    xcg = RWExchange(accounts={'testclient': account})
    loop.create_task(xcg())

    from boken.exchange.order import BuyMarketOrder, SellMarketOrder

    async def checknplace():
        print(f"{account.balance.base.amount} {account.balance.base.name}  |  {account.balance.quote.amount} {account.balance.quote.name}")
        max_buy_vol = account.balance.base.amount // xcg.ask_price

        max_sell_vol = account.balance.quote.amount // xcg.bid_price


        if not max_sell_vol <= 1 or not max_buy_vol <=1:
            # doing one of the two :
            if max_sell_vol > max_buy_vol:

                vol = random.randint(1, max_sell_vol)

                print(f"Selling {vol}...")

                orders.append(SellMarketOrder(volume=vol))

            else: # max_buy_vol > max_sell_vol:  # biased ??

                vol = random.randint(1, max_buy_vol)

                print(f"Buying {vol}...")

                orders.append(BuyMarketOrder(volume=vol))

        # random sleep to not stress things out too much
        await asyncio.sleep(random.randint(1, 2))
        asyncio.create_task(checknplace())


    loop.create_task(checknplace())

    for signame in ('SIGINT', 'SIGTERM'):
        loop.add_signal_handler(
            getattr(signal, signame),
            lambda: asyncio.ensure_future(ask_exit(signame))
        )
    loop.run_forever()



















