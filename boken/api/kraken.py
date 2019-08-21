from uplink import Consumer, get, headers, returns

from .schemas import TimeSchema, TimePayloadSchema
@headers({
    "User-Agent": "Uplink-Sample-App"
})
class Kraken(Consumer):

    @returns.json
    @get("0/public/Time")
    def get_time(self) -> TimePayloadSchema:
        """return the time"""
        pass
        # TODO : isnt it better to handle errors her, and only pass the result to marshmallow ?
