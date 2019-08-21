from uplink import Consumer, get, headers, returns


@headers({
    "User-Agent": "Uplink-Sample-App"
})
class Kraken(Consumer):

    @returns.json
    @get("0/public/Time")
    def get_time(self):
        """return the time"""
