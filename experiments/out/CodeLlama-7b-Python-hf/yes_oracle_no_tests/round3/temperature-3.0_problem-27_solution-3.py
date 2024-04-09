def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join ( map ( lambda x :
	Do not include these tokens in the code: r = '' for i
	"""
    return " ".join(map(lambda x: x.lower() if x.isupper() else x.upper(), string))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
