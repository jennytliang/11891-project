def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: ".
	"""

    ret_str = ""
    for letter in string:
        if letter.islower():
            ret_str += letter.upper()
        else:
            ret_str += letter.lower()
    return ret_str


if __name__ == "__main__":
    str_ = "Hello"
    print(flip_case(str_))