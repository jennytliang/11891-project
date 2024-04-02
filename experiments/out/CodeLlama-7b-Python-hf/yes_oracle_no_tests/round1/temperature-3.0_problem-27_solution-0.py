def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    r = list(string)
    for i in range(len(r)):
        if r[i].islower():
            r[i] = r[i].upper()
        elif r[i].isupper():
            r[i] = r[i].lower()
    return " ".join(r)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
