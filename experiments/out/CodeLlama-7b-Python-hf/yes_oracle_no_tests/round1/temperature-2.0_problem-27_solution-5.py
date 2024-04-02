def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    r = ""
    for i in string:
        if i.islower():
            r += i.upper()
        elif i.isupper():
            r += i.lower()
        else:
            r += i
    return r


def flip_case_one_liner(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    return " ".join(map(lambda x: x.lower() if x.isupper() else x.upper(), string))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
