def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: ".
	"""

    ret = ''
    for letter in string:
        if letter.islower():
            ret += letter.upper()
        else:
            ret += letter.lower()
    return ret


if __name__ == '__main__':
    import doctest
    doctest.testmod()
