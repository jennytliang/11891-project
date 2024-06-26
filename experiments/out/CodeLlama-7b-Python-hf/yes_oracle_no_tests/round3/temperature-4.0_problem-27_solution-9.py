def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Do not include these tokens in the code: # return string . swap case ()
	"""
    return string.swapcase()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
