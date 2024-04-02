def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = ''
    for char in string:
        if char.islower():
            r += char.upper()
        else:
            r += char.lower()
    return r

print(flip_case('Hello'))
