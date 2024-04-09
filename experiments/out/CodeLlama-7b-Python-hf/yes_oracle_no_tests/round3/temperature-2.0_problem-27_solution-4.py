def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: ".
	"""

    ret = ''
    for i in string:
        if i.islower():
            ret += i.upper()
        elif i.isupper():
            ret += i.lower()
        else:
            ret += i
    return ret


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
    print(flip_case('Hello'))
    print(flip_case_2('Hello'))
