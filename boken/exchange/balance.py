"""
Model of an account
"""
from dataclasses import dataclass


@dataclass
class Currency:
    name: str
    amount: int


@dataclass
class Balance:
    #TMP : relative to only one absolute market for now...
    quote: Currency
    base: Currency
