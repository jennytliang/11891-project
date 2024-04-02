def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = ""
    for i in range(n + 1):
        if i != n:
            r += str(i) + " "
        else:
            r += str(i)
    return r



def string_sequence_with_for(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = ""
    for i in range(n + 1):
        if i == 0:
            r += str(i)
        elif i == n:
            r += " " + str(i)
        else:
            r += " " + str(i) + " "
    return r



def string_sequence_with_while(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = ""
    i = 0
    while i <= n:
        if i == 0:
            r += str(i)
        elif i == n:
            r += " " + str(i)
        else:
            r += " " + str(i) + " "
        i += 1
    return r



def string_sequence_with_for_and_while(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 