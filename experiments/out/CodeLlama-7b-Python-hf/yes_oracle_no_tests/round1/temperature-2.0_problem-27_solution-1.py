def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    r = []
    for c in string:
        if c.islower():
            r.append(c.upper())
        else:
            r.append(c.lower())
    return ' '.join(r)

    # alternatively
    # return ' '.join(map(lambda x: x.upper() if x.islower() else x.lower(), string.split()))


if __name__ == '__main__':
    print('Example:')
    print(flip_case('Python'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert flip_case('Python') == 'pYthON'
    assert flip_case('hELLO') == 'HeLLo'
    assert flip_case('12345') == '12345'
    assert flip_case('aaa') == 'AAA'
    print('You are awesome! All tests are done! Go Check it!')
