def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: ".
	"""

    ret_str = ""
    for char in string:
        if char.islower():
            ret_str += char.upper()
        else:
            ret_str += char.lower()
    return ret_str


if __name__ == "__main__":
    input_string = "Hello"
    print(flip_case(input_string))
