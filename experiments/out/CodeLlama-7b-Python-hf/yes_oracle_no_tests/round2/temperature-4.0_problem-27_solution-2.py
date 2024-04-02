def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: ".
	"""

    ret = ''
    for char in string:
        if char.islower():
            char = char.upper()
        elif char.isupper():
            char = char.lower()
        ret += char
    return ret


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print(flip_case(input_string))
