def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Do not include these tokens in the code: # solution target
	"""
    # [i for i in range(n+1)]
    # ' '.join([str(i) for i in range(n+1)])
    # ' '.join(str(i) for i in range(n+1))
    return ' '.join(map(str, range(n + 1)))


def string_sequence2(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Do not include these tokens in the code: # solution target
	"""
    # if n == 0:
    #     return '0'
    # return ' '.join(str(i) for i in range(n + 1))
    return ' '.join(str(i) for i in range(n + 1)) if n != 0 else '0'


print(string_sequence2(5))
