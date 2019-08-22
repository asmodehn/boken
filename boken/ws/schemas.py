import marshmallow.validate
import typing

from ..errors import BokenException
from ..model.time import Time

from .subscription import Subscription
from .heartbeat import Heartbeat
from .pingpong import Ping, Pong


class SchemaBase(marshmallow.Schema):
    class Meta:
        # Pass EXCLUDE as Meta option to keep marshmallow 2 behavior
        # ref: https://marshmallow.readthedocs.io/en/3.0/upgrading.html
        unknown = getattr(marshmallow, "EXCLUDE", None)


class PingSchema(SchemaBase):
    """Schema to build the data sent for Ping"""

    event: str = marshmallow.fields.Str(required=True,
        validate=marshmallow.validate.Regexp(
            '^ping$',
            error='ping is invalid'
        ))
    reqid: typing.Optional[int]

    # load or dump ?
    @marshmallow.post_load(pass_many=False)
    def make_ping(self, data, **kwargs):
        return Ping()


class PongSchema(SchemaBase):
    """ Schema to parse the data received for pong"""

    event: str = marshmallow.fields.Str(required=True,
        validate=marshmallow.validate.Regexp(
            '^pong$',
            error='pong is invalid'
        ))
    reqid: typing.Optional[int]

    # load or dump ?
    @marshmallow.post_load(pass_many=False)
    def make_pong(self, data, **kwargs):
        return Pong()


class HeartbeatSchema(SchemaBase):
    """ Schema to parse te data received for heartbeat"""
    event: str = marshmallow.fields.Str(required=True,
        validate=marshmallow.validate.Regexp(
            '^heartbeat$',
            error='heartbeat is invalid'
        ))

    @marshmallow.post_load(pass_many=False)
    def make_sub(self, data, **kwargs):
        return Heartbeat()


class SubscriptionSchema(SchemaBase):
    """ Schema to parse the data received"""

    depth: typing.Optional[int]
    interval: typing.Optional[int]
    token: typing.Optional[int]
    name: str

    @marshmallow.post_load(pass_many=False)
    def make_sub(self, data, **kwargs):
        return Subscription(data.get("unixtime"))


# == Schemas == #
# TODO : reuse this for other kind of payload data ?
class SubscriptionPayloadSchema(marshmallow.Schema):

    event: str = marshmallow.fields.Str(default="subscribe")
    reqid: int
    # TODO : proper Pair type
    pair: typing.List[str]
    subscription: Subscription = marshmallow.fields.Nested(SubscriptionSchema)

    @marshmallow.post_load(pass_many=False)
    def filter_error(self, data, **kwargs):
        if len(data.get("error")) > 0: # TODO : currently buggy on error (silent retry ?). TOFIX
            raise BokenException("ERROR in message from server: " + data.get("error"))
        else:
            # just get the result
            return data.get("result")



if __name__ == '__main__':
    # TODO : run doc test on these...
    pass