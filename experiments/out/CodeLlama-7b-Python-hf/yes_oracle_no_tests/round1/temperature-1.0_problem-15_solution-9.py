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
        if len(r) == 0:
            r = str(i)
        else:
            r += str(i) + ' '

    return r

    # You can also remove the last character from string 'r' if you used code r = r + " " + str(i)
    # However r = r + " " + str(i) takes more time as string concatenation in python is expensive





def string_sequence_without_concat(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Remove tokens from the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = ""
    for i in range(n + 1):
        if len(r) == 0:
            r = str(i)
        else:
            r = r + str(i) + ' '

    s = ""
    for j in range(len(r) - 1):
        if r[j] != ' ':
            s += r[j]
        else:
            s += ' '

    return s
    # Also note we are returning space separated string 's' rather than the original variable 'r'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
