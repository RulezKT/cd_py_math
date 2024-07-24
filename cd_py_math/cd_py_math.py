import math
from cd_py_consts import RAD_RATIO


def fractions_into_degrees(degrees: float) -> tuple[float, float, float]:
    """
    ENG:
    Conversion of degrees and fractions of degree into
    degrees, minutes and seconds

    DEU:
    Umrechnung von Grad und Bruchteilen eines Grades
    in Grad, Minuten und Sekunden.

    RUS:
    Преобразование градусов и доли градусов,
    в градусы минуты и секунды

    """

    # https://stackoverflow.com/questions/2579535/convert-dd-decimal-degrees-to-dms-degrees-minutes-seconds-in-python

    # divmod() method takes two numbers as arguments and returns their quotient and remainder in a tuple.

    mult = -1 if degrees < 0 else 1
    mnt, sec = divmod(abs(degrees) * 3600, 60)
    deg, mnt = divmod(mnt, 60)
    return (mult * deg, mult * mnt, mult * sec)


def degrees_into_fractions(degrees, minutes, seconds):
    """
    ENG:
    conversion of degrees, minutes and seconds into
    degrees and fractions of degree

    DEU:
    Umwandlung von Grad, Minuten und Sekunden in
    Grad und Bruchteile des Grades

    RUS:
    Преобразование градусов, минут и секунд в
    градусы и доли градусов

    """

    sign = -1.0 if (degrees < 0 or minutes < 0 or seconds < 0) else 1.0

    return sign * (abs(degrees) + abs(minutes) / 60.0 + abs(seconds) / 3600.0)


# equivalent math.atan2(y,x)*(180/math.pi)
def atan2_in_degrees(y, x):
    if x == 0 and y == 0:
        return 0
    else:
        abs_x = abs(x)
        abs_y = abs(y)
        if abs_x > abs_y:
            phi = math.atan(abs_y / abs_x) / RAD_RATIO
        else:
            phi = 90 - math.atan(abs_x / abs_y) / RAD_RATIO

        if x < 0:
            phi = 180 - phi

        if y < 0:
            phi = -phi
    return phi


# убирает минус или значения больше 360
# если угол должен быть от 0 до 360
# все в Радианах
def convert_to_0_360_RAD(longitude):
    coeff = abs(math.trunc(longitude / (2 * math.pi)))
    return (
        longitude + coeff * 2 * math.pi + 2 * math.pi
        if longitude < 0
        else longitude - coeff * 2 * math.pi
    )


# убирает минус или значения больше 360
# если угол должен быть от 0 до 360
# все в Градусах
def convert_to_0_360_DEG(longitude):
    coeff = abs(math.trunc(longitude / 360))
    return longitude + coeff * 360 + 360 if longitude < 0 else longitude - coeff * 360
