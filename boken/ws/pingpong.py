from dataclasses import dataclass, field

import typing

""" Ping Pong """


@dataclass(frozen=True)
class Ping:
    reqid: typing.Optional[int] = field(init=False)


@dataclass(frozen=True)
class Pong:
    reqid: typing.Optional[int] = field(init=False)
