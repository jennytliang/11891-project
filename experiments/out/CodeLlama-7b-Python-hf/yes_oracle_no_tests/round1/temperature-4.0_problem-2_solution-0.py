def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: if number >= 1 :
	"""
    if number >= 1:
        return 0
    else:
        return number % 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
