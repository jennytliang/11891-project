def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join ( map ( lambda x :
	"""
    return " ".join(map(lambda x: x.upper() if x.islower() else x.lower(), string))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
