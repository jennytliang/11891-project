def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    return " ".join(str(num) for num in range(n + 1)) 


print(string_sequence(10))

def int_pair(n: int) -> (int,int): 
    """ Returns a tuple pair with the same value
        >>> int_pair(5) == (5,5)
        True
    """