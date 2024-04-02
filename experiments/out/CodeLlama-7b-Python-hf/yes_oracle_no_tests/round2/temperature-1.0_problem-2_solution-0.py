def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
	Include these tokens in the code: number
	Do not include these tokens in the code: num b
	"""


    return number  - int(number)

assert truncate_number(3.5) == 0.5
assert truncate_number(5.0) == 0.0
assert truncate_number(1.2) == 0.2
assert truncate_number(4.7) == 0.7
assert truncate_number(4.2) == 0.2
assert truncate_number(4) == 0
assert truncate_number(1.0) == 0.0
assert truncate_number(2.0) == 0.0
assert truncate_number(1.01) == 0.01
assert truncate_number(0.01) == 0.01


def truncate_number_2(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
	Include these tokens in the code: number
	Do not include these tokens in the code: num b
	"""


    return number - int(number)

assert truncate_number_2(3.5) == 0.5
assert truncate_number_2(5.0) == 0.0
assert truncate_number_2(1.2) == 0.2
assert truncate_number_2(4.7) == 0.7
assert truncate_number_2(4.2) == 0.2
assert truncate_number_2(4) == 0
assert truncate_number_2(1.0) == 0.0
assert truncate_number_2(2.0) == 0.0
assert truncate_number_2(1.01) == 0.01
assert truncate_number_2(0.01) == 0.01
