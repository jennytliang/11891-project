def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
	Include these tokens in the code: number
	Do not include these tokens in the code: num
	"""



    return number - int(number)

def main():
    """ This main function will not be called if this code is being imported
    to another module.
    """
    print(truncate_number(3.5))

if __name__ == '__main__':
    main()

