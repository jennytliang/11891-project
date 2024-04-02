def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r tn = ""
	"""
    
    tn = ""
    for n in range(n + 1):
        tn += str(n) + ' '
    return tn[:-1]