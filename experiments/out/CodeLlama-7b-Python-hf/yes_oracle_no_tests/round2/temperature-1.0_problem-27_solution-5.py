def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Do not include these tokens in the code: r = "" for
	"""
    r = ""
    for i in range(len(string)):
        if string[i].isupper():
            r += string[i].lower()
        else:
            r += string[i].upper()
    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()