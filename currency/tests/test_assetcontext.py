import decimal
import unittest

import hypothesis.strategies as st
from hypothesis import given

from currency.assetcontext import AssetContext


@st.composite
def context_strategy(draw):
    prec = draw(st.integers(min_value=1, max_value=decimal.MAX_PREC))
    rounding = draw(
        st.sampled_from(
            [
                None,
                decimal.ROUND_DOWN,
                decimal.ROUND_HALF_UP,
                decimal.ROUND_HALF_EVEN,
                decimal.ROUND_CEILING,
                decimal.ROUND_FLOOR,
                decimal.ROUND_UP,
                decimal.ROUND_HALF_DOWN,
                decimal.ROUND_05UP,
            ]
        )
    )
    traps = draw(
        st.lists(
            elements=st.sampled_from(
                [
                    decimal.Clamped,
                    decimal.InvalidOperation,
                    decimal.DivisionByZero,
                    decimal.Inexact,
                    decimal.Rounded,
                    decimal.Subnormal,
                    decimal.Overflow,
                    decimal.Underflow,
                    decimal.FloatOperation,
                ]
            ),
        )
    )
    flags = draw(
        st.lists(
            elements=st.sampled_from(
                [
                    decimal.Clamped,
                    decimal.InvalidOperation,
                    decimal.DivisionByZero,
                    decimal.Inexact,
                    decimal.Rounded,
                    decimal.Subnormal,
                    decimal.Overflow,
                    decimal.Underflow,
                    decimal.FloatOperation,
                ]
            ),
        )
    )
    Emin = draw(st.integers(min_value=decimal.MIN_EMIN, max_value=0),)
    Emax = draw(st.integers(min_value=0, max_value=decimal.MAX_EMAX),)
    capitals = draw(st.sampled_from([0, 1]),)
    clamp = draw(st.sampled_from([0, 1]))

    return AssetContext(
        prec=prec,
        rounding=rounding,
        traps=traps,
        flags=flags,
        Emin=Emin,
        Emax=Emax,
        capitals=capitals,
        clamp=clamp,
    )


@st.composite
def context_mutation_strategy(draw):
    fieldchange = draw(
        st.sampled_from(
            [
                "prec",
                "rounding",  #'traps', 'flags',
                "Emin",
                "Emax",
                "capitals",
                "clamp",
            ]
        )
    )

    mutation = {fieldchange: None}
    # one slight modification make them not equal
    if fieldchange == "prec":
        mutation[fieldchange] = draw(
            st.integers(min_value=1, max_value=decimal.MAX_PREC)
        )
    elif fieldchange == "rounding":
        mutation[fieldchange] = draw(
            st.sampled_from(
                [
                    decimal.ROUND_DOWN,
                    decimal.ROUND_HALF_UP,
                    decimal.ROUND_HALF_EVEN,
                    decimal.ROUND_CEILING,
                    decimal.ROUND_FLOOR,
                    decimal.ROUND_UP,
                    decimal.ROUND_HALF_DOWN,
                    decimal.ROUND_05UP,
                ]
            )
        )
    # TMP :disabled : internal dictionary structure not obvious from outside...
    # elif fieldchange == 'traps':
    #     mutation[fieldchange] = draw(st.lists(elements=st.sampled_from([decimal.Clamped, decimal.InvalidOperation, decimal.DivisionByZero,
    #                                            decimal.Inexact, decimal.Rounded, decimal.Subnormal, decimal.Overflow, decimal.Underflow, decimal.FloatOperation]),))
    # elif fieldchange == 'flags':
    #     mutation[fieldchange] = draw(st.lists(elements=st.sampled_from([decimal.Clamped, decimal.InvalidOperation, decimal.DivisionByZero,
    #                                            decimal.Inexact, decimal.Rounded, decimal.Subnormal, decimal.Overflow, decimal.Underflow, decimal.FloatOperation]),))
    elif fieldchange == "Emin":
        mutation[fieldchange] = draw(
            st.integers(min_value=decimal.MIN_EMIN, max_value=0),
        )
    elif fieldchange == "Emax":
        mutation[fieldchange] = draw(
            st.integers(min_value=0, max_value=decimal.MAX_EMAX),
        )
    elif fieldchange == "capitals":
        mutation[fieldchange] = draw(st.sampled_from([0, 1]))
    elif fieldchange == "clamp":
        mutation[fieldchange] = draw(st.sampled_from([0, 1]))

    return mutation


class TestAssetContext(unittest.TestCase):
    @given(contexta=context_strategy(), contextb=context_strategy())
    def test_eq_values(self, contexta, contextb):
        # Reflexivity of equality
        assert contexta == contexta
        assert contextb == contextb

        # equivalence relation with tuple equality
        if (
            contexta.prec,
            contexta.rounding,
            contexta.traps,
            contexta.flags,
            contexta.Emin,
            contexta.Emax,
            contexta.capitals,
            contexta.clamp,
        ) == (
            contextb.prec,
            contextb.rounding,
            contextb.traps,
            contextb.flags,
            contextb.Emin,
            contextb.Emax,
            contextb.capitals,
            contextb.clamp,
        ):
            assert contexta == contextb

        if contexta == contextb:
            assert (
                contexta.prec,
                contexta.rounding,
                contexta.traps,
                contexta.flags,
                contexta.Emin,
                contexta.Emax,
                contexta.capitals,
                contexta.clamp,
            ) == (
                contextb.prec,
                contextb.rounding,
                contextb.traps,
                contextb.flags,
                contextb.Emin,
                contextb.Emax,
                contextb.capitals,
                contextb.clamp,
            )

    @given(context=context_strategy(), mutation=context_mutation_strategy())
    def test_ne_values(self, context, mutation):
        import copy

        contextb = copy.copy(context)

        # copy are equals
        assert contextb == context

        # one slight modification make them not equal
        for m, v in mutation.items():
            if getattr(contextb, m) == v:  # changing must preserve equality...
                setattr(contextb, m, v)
                assert contextb == context
            else:  # changing should break equality
                setattr(contextb, m, v)
                assert contextb != context


if __name__ == "__main__":
    unittest.main()
