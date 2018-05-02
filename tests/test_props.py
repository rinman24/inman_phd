
import math

from chamber import props

P_VALUE = 101325
T_VALUE = 290
TDP_VALUE = 280


def test_cpm():
    assert math.isclose(
        props.cpm(P_VALUE, T_VALUE, TDP_VALUE),
        1017.641910841458
        )
    