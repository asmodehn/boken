import typing
from dataclasses import dataclass, field



#TODO : better representation & typing fo this... (similar to whatever we use for hte REST API data)


@dataclass()
class Subscription:
    name: str
    depth: typing.Optional[int] = None
    interval: typing.Optional[int] = None
    token: typing.Optional[int] = None


@dataclass()
class SubscriptionPayload:
    reqid: int
    # TODO : proper Pair type
    pair: typing.List[str]
    subscription: Subscription
    event: str = field(default="subscribe", init=False)

