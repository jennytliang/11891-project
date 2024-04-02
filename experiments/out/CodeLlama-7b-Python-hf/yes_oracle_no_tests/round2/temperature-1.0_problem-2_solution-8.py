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


    return number 
    num, decimals = str(number).split('.')
    b = len(decimals)
    if(num !=0):   
        return float('.'.join([num[-1:], decimals]))
    else:
        return float('.'.join([num[0], decimals]))

    raise NotImplementedError


if __name__ == "__main__":
    import doctest
    doctest.testmod()
