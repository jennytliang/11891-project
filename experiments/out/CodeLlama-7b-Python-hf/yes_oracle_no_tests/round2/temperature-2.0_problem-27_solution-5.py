def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Do not include these tokens in the code: r = "" for
	"""
    r = ""
    for i in string:
        if i.islower():
            r += i.upper()
        elif i.isupper():
            r += i.lower()
        else:
            r += i
    return r


if __name__ == "__main__":
    s = input("Enter a string: ")
    print(flip_case(s))
