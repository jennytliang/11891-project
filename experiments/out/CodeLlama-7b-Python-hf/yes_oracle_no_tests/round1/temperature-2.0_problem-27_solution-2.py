def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    r = " ".join(map(lambda x: x.lower() if x.isupper() else x.upper(), string))
    return r


def flip_case_2(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    r = " ".join(map(lambda x: x.upper() if x.islower() else x.lower(), string.split(" ")))
    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
