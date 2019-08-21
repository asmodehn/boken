


class Time:
    """
    A cross exchange python representation of time.
    Includes domain specific semantic about correctness of data.
    """

    def __init__(self, unixtime):
        self._unixtime = unixtime


    @property
    def unixtime(self):
        return self._unixtime

