def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    r = ' '.join(map(lambda x: x.lower() if x.isupper() else x.upper(),string)).title()
    return r

print(flip_case('Hello'))
print(flip_case('wHaT aBiT'))
print(flip_case("can't"))
print(flip_case('The SKY is Falling'))

def flip_case(string):
   """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
        >>> flip_case('Hello')
        'hELLO'
    
        Include these tokens in the code: " ". join ( map ( lambda x : x
        Do not include these tokens in the code: string
    """

    return ' '.join(map(lambda x: x.lower() if x.isupper() else x.upper(),string)).title()
