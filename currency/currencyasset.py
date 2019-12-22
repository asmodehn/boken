from dataclasses import dataclass

from currency.asset import Asset

@dataclass(frozen=True)
class Currency(Asset):
    """ Just an Asset that can be used as price unit """
    pass
