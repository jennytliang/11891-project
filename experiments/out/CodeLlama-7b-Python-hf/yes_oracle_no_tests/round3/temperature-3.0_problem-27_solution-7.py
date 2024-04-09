def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join ( map ( lambda x :
	Do not include these tokens in the code: r = '' for char
	"""
    # r = ''
    # for char in string:
    #     if char.isupper():
    #         r += char.lower()
    #     else:
    #         r += char.upper()
    # return r
    return " ".join(map(lambda x: x.lower() if x.isupper() else x.upper(), string.split()))


if __name__ == "__main__":
    str_test = "hello"
    print(flip_case(str_test))
