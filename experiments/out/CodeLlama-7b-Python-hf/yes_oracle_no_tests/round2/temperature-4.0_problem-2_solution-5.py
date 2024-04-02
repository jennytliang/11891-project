def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
	Do not include these tokens in the code: if number >= 1 :
	"""
    # truncate the number
    # if the number is smaller than 1, it is the decimal part
    if number < 1:
        return number
    else:
        return number - int(number)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
