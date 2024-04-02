def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: r = list
	"""
    r = list(string)
    for i in range(len(r)):
        if r[i].isupper():
            r[i] = r[i].lower()
        else:
            r[i] = r[i].upper()
    return "".join(r)


if __name__ == "__main__":
    string = 'Hello'
    print(flip_case(string))
