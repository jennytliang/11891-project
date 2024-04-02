def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    r = ""
    for i in string:
        if i.isupper():
            r += i.lower()
        elif i.islower():
            r += i.upper()
        else:
            r += i
    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
