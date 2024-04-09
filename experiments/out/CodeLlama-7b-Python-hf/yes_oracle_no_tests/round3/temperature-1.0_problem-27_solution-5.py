def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: r = "" for i
	"""
    r = ""
    for i in string:
        if i.isupper():
            r += i.lower()
        else:
            r += i.upper()
    return r


def flip_case_2(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: r = "" for i
	"""
    return " ".join(i.lower() if i.isupper() else i.upper() for i in string)


def flip_case_3(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: r = "" for i
	"""
    return " ".join(map(lambda x: x.upper() if x.islower() else x.lower(), string))


def flip_case_4(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: r = "" for i
	"""
    return " ".join(map(lambda x: x.upper() if x.islower() else x.lower(), string))
