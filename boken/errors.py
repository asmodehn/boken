
# Ref : https://julien.danjou.info/python-exceptions-guide/


class BokenException(Exception):
    """Base class for Boken's exceptions
    """

    def __init__(self, msg=None, fixer=None, original=None):
        """Initializes a Boken exception.
        Optionally can wrap another exception"""
        msg = "Boken Exception !" if msg is None else msg
        if original:
            self.original = original
            super().__init__(f"{msg}: {original}")
        else:
            super().__init__(f"{msg}")

        # Dynamically build a method to address this exception
        self.fixme = fixer


class ExchangeError(BokenException):
    pass


class AuthenticationError(ExchangeError):
    pass


class PermissionDenied(AuthenticationError):
    pass


class AccountSuspended(AuthenticationError):
    pass
