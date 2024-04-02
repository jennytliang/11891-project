def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    rtn = ""
    for c in string:
        if c.isupper():
            rtn += c.lower()
        else:
            rtn += c.upper()
    return rtn


def flip_case_2(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'

	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    return " ".join(map(lambda x: x.upper() if x.islower() else x.lower(), string))


def flip_case_3(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'

	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    return " ".join(map(lambda c: c.lower() if c.isupper() else c.upper(), string))


def flip_case_4(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'

	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    return " ".join(map(lambda x: x.swapcase(), string))


def flip_case_5(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'

	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: