import decimal


class AssetContext(decimal.Context):
    """ Just a decimal context, that can be compared with others"""

    def __eq__(self, other):

        return (
            self.prec,
            self.rounding,
            self.traps,
            self.flags,
            self.Emin,
            self.Emax,
            self.capitals,
            self.clamp,
        ) == (
            other.prec,
            other.rounding,
            other.traps,
            other.flags,
            other.Emin,
            other.Emax,
            other.capitals,
            other.clamp,
        )
