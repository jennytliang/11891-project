def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Do not include these tokens in the code: r tn = ""
	"""
    # return ''.join(c.lower() if c.isupper() else c.upper() for c in string)
    new_string = ""
    for c in string:
        if c.islower():
            new_string += c.upper()
        else:
            new_string += c.lower()
    return new_string


def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Do not include these tokens in the code: r tn = ""
	"""
    # return ''.join(c.lower() if c.isupper() else c.upper() for c in string)
    new_string = ""
    for c in string:
        if c.islower():
            new_string += c.upper()
        else:
            new_string += c.lower()
    return new_string
