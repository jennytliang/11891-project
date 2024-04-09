def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: ".
	"""

    ret_str = ''
    for char in string:
        if char.islower():
            ret_str += char.upper()
        elif char.isupper():
            ret_str += char.lower()
        else:
            ret_str += char
    return ret_str


def main():
    str_val = 'Hello'
    print(flip_case(str_val))


if __name__ == "__main__":
    main()
