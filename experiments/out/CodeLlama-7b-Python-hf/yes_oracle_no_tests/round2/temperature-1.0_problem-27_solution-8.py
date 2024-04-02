def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join ( map ( lambda x :
	"""
    return " ".join(map(lambda x: x.swapcase(),string))
    #" ".join(map)