def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: ".
	"""

    ret_str = ""
    for char in string:
        if char.isupper():
            ret_str += char.lower()
        else:
            ret_str += char.upper()
    return ret_str


def flip_case_2(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: ".
	"""

    return string.swapcase()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
