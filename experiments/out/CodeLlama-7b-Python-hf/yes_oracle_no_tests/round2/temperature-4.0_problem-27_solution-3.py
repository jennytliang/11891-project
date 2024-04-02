def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: ".
	"""

    ret = ""
    for c in string:
        if c.islower():
            ret += c.upper()
        else:
            ret += c.lower()
    return ret


if __name__ == "__main__":
    str = input("Enter string: ")
    print(flip_case(str))
