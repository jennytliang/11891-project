def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: # result = '' #
	"""
    return " ".join(c.lower() if c.isupper() else c.upper() for c in string)


if __name__ == "__main__":
    input_string = "Hello"
    print(flip_case(input_string))