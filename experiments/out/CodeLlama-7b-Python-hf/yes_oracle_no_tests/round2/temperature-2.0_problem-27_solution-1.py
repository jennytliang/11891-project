def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Do not include these tokens in the code: r = [] for
	"""
    # Your code here
    r = string.swapcase()
    return r


if __name__ == "__main__":
    str = 'Hello'
    print(flip_case(str))
