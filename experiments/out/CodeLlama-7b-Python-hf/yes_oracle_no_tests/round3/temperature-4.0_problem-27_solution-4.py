def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join ( map ( lambda x :
	Do not include these tokens in the code: result = '' for i
	"""
    
    # return " ".join(map(lambda x: x.lower() if x.isupper() else x.upper(), string.split()))
    return " ".join(map(lambda x: x.lower() if x.isupper() else x.upper(), string.split()))
    
    # result = ''
    # for i in string:
    #     if i.isupper():
    #         i = i.lower()
    #     else:
    #         i = i.upper()
    #     result += i
    # return result
    
    