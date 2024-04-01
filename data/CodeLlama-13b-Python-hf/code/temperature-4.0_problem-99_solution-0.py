def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    # A float represents the absolute difference
    if value[:1] == "-":
        int_value = int((float(value) - 0.1) // 1) # int = -5.8 = -6.0
        print(" - abs_value {} ".format(abs(value)))

    else:
        int_value = int(value + 0.5) # int = abs(-5.8 or 6.0) or 5 and 6
        raise NotImplementedError
    # value_from_zero is a list with the integer and the absolute_difference
    value_from_zero: list(int_number, abs_distance) = [int_value, abs(value -  int)]
    return int_value
############################################################ INITIAL TESTING ###############################
import pytest

@pytest.mark.parametrize('arg1, expected', [
    ('-2.7', -3), ('1', 1),
])
def test_closest_integer_1(arg1, expected):
    # test_case = {"abr": [2, [['1.5', '2.5'], ['-10', '-2.1']], True], "assertion": [-2, [['1.5'], ['-10']]], "position": [1], "message": "Expected -2." }
    # test case
    actual = closest_integer(arg1,)

    # testing the value
    # actual -> 1 actual value from method
    # expected or gold -> the excepted value from the method
    # assert < actual value or > <expected value > <error message>, < <position>
