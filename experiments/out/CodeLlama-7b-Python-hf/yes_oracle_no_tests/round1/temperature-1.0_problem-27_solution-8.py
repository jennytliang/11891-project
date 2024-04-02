def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    rtnVal = ""
    for char in string:
        if (char.islower()):
            rtnVal = rtnVal + char.upper()
        elif (char.isupper()):
            rtnVal = rtnVal + char.lower()
        else:
            rtnVal = rtnVal + char
    return rtnVal
            

if __name__ == "__main__":
    import doctest
    doctest.testmod()