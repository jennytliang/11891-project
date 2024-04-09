def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join ( map ( lambda x :
	Do not include these tokens in the code: r = "" for char
	"""
    return " ".join(map(lambda x: x.upper() if x.islower() else x.lower(), string))


def flip_case_2(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
    """
    r = ""
    for char in string:
        if char.islower():
            r += char.upper()
        else:
            r += char.lower()
    return r


def flip_case_3(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
    """
    r = ""
    for char in string:
        if char.islower():
            r += char.upper()
        else:
            r += char.lower()
    return r


def flip_case_4(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
    """
    r = ""
    for char in string:
        if char.islower():
            r += char.upper()
        else:
            r += char.lower()
    return r


def flip_case_5(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
    """
    r = ""
    for char in string:
        if char.islower():
            r += char.upper()
        else:
            r += char.lower()
    return r


def flip_case_6(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase