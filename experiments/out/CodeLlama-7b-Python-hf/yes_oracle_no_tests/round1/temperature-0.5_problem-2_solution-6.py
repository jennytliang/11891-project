def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    return number - int(number)


i = 0

while True:
    i += 1
    if truncate_number(i) < 0.1:
        break

print(i)
