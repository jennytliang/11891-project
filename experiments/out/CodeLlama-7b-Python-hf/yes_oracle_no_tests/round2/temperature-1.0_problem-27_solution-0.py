def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ".
	Do not include these tokens in the code: r = ' '.
	"""

    r = ""
    for ch in string:
        # The 'lower' method makes this lower case.
        if ch.isupper() is True:
            r += ch.lower()
        # The 'upper' method makes this upper case.
        if ch.islower() is True:
            r = r + ch.upper()

    return r

if __name__ == '__main__':
    print('Experimenting...')
    s = 'Hello'
    print("s:", s)
    r = flip_case(s)
    print("r:", r)
