import math
from math_funcs import fractions_into_degrees, atan2_in_degrees


def test_fractions_into_degrees():
    assert fractions_into_degrees(0.5) == (0, 30, 0)
    assert fractions_into_degrees(0.25) == (0, 15, 0)
    assert fractions_into_degrees(0.75) == (0, 45, 0)
    assert fractions_into_degrees(0.125) == (0, 7, 30)
    assert fractions_into_degrees(0.875) == (0, 52, 30)
    assert fractions_into_degrees(0.0625) == (0, 3, 45)
    assert fractions_into_degrees(0.9375) == (0, 56, 15)
    assert fractions_into_degrees(0.96875) == (0, 58, 7.5)
    assert fractions_into_degrees(25.96875) == (25, 58, 7.5)
    assert fractions_into_degrees(-25.96875) == (-25, -58, -7.5)
    assert fractions_into_degrees(370.96875) == (370, 58, 7.5)


def test_atan2_in_degrees():
    assert atan2_in_degrees(0, 0) == 0
    assert atan2_in_degrees(1, 1) == 45
    assert atan2_in_degrees(-1, 1) == -45
    assert atan2_in_degrees(1, -1) == 135
    assert atan2_in_degrees(-1, -1) == -135
    assert atan2_in_degrees(1, 0) == 90
    assert atan2_in_degrees(-1, 0) == -90
    assert atan2_in_degrees(0, 1) == 0
    assert atan2_in_degrees(0, -1) == 180

    assert atan2_in_degrees(0, 0) == math.atan2(0, 0) * (180 / math.pi)
    assert atan2_in_degrees(1, 1) == math.atan2(1, 1) * (180 / math.pi)
    assert atan2_in_degrees(-1, 1) == math.atan2(-1, 1) * (180 / math.pi)
    assert atan2_in_degrees(1, -1) == math.atan2(1, -1) * (180 / math.pi)
    assert atan2_in_degrees(-1, -1) == math.atan2(-1, -1) * (180 / math.pi)
    assert atan2_in_degrees(1, 0) == math.atan2(1, 0) * (180 / math.pi)
    assert atan2_in_degrees(-1, 0) == math.atan2(-1, 0) * (180 / math.pi)
    assert atan2_in_degrees(0, 1) == math.atan2(0, 1) * (180 / math.pi)
    assert atan2_in_degrees(0, -1) == math.atan2(0, -1) * (180 / math.pi)
