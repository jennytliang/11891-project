def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
	Include these tokens in the code: return number - int
	Do not include these tokens in the code: integer , decimal = str
	"""
    return number - int(number)

def main():
    import doctest
    doctest.testmod()
    print(truncate_number(3.5))
    print(truncate_number(0.99))
    print(truncate_number(1.0))
    print(truncate_number(1.1))
    print(truncate_number(3.99999))

if __name__ == "__main__":
    main()
