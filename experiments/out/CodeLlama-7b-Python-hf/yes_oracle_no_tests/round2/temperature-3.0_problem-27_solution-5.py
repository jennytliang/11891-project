def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ".
	Do not include these tokens in the code: r = ' '.
	"""
    r = ""
    for char in string:
        if char.islower():
            r += char.upper()
        else:
            r += char.lower()
    return r


if __name__ == "__main__":
    print("Example:")
    print(flip_case("Example"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert flip_case("Example") == "eXAMPLE"
    assert flip_case("a") == "A"
    assert flip_case("AAbb") == "aAbb"
    print("Coding complete? Click 'Check' to earn cool rewards!")
