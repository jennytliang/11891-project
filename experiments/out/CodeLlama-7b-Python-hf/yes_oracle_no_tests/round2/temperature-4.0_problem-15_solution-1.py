def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return " ". join ( map ( str , range
	"""
    return " ".join(map(str, range(n + 1)))


def string_sequence_join(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_join(0)
    '0'
    >>> string_sequence_join(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return " ". join ( map ( str , range
    """
    return " ".join(map(str, range(n + 1)))


def string_sequence_comprehension(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_comprehension(0)
    '0'
    >>> string_sequence_comprehension(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return " ". join ( map ( str , range
    """
    return " ".join(str(i) for i in range(n + 1))


def string_sequence_comprehension_no_join(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_comprehension_no_join(0)
    '0'
    >>> string_sequence_comprehension_no_join(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: return " ". join ( map ( str , range
    """
    return " ".join(str(i) for i in range(n + 1))


def string_sequence_comprehension_no_join_no_space(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence_comprehension_no_join_no_space(0)
   