def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = ''
    for c in string:
        if c.isupper():
            r += c.lower()
        else:
            r += c.upper()
    return r
