def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return " ".
	Do not include these tokens in the code: r = ' '.
	"""
    return ' '.join(str(i) for i in range(n + 1))


def string_sequence2(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence2(0)
    '0'
    >>> string_sequence2(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return " ".
	Do not include these tokens in the code: r = ' '.
	"""
    r = ''
    for i in range(n + 1):
        if i == 0:
            r = str(i)
        else:
            r += ' ' + str(i)
    return r


def string_sequence3(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence3(0)
    '0'
    >>> string_sequence3(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return " ".
	Do not include these tokens in the code: r = ' '.
	"""
    r = ''
    for i in range(n + 1):
        r += ' ' + str(i)
    return r[1:]


def string_sequence4(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence4(0)
    '0'
    >>> string_sequence4(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return " ".
	Do not include these tokens in the code: r = ' '.
	"""
    return ' '.join(str(i) for i in range(n + 1))


def string_sequence5(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n