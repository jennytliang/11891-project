def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    r = ''
    for c in string:
        if c.isupper():
            r += c.lower()
        else:
            r += c.upper()
    return r


def flip_case2(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    return ' '.join(map(lambda x: x.upper() if x.islower() else x.lower(), string))


def main():
    str = 'Hello'
    print(flip_case(str))
    print(flip_case2(str))


if __name__ == '__main__':
    main()
