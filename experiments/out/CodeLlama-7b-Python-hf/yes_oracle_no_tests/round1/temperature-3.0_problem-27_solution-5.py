def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
	Include these tokens in the code: " ". join ( map ( lambda x : x
	Do not include these tokens in the code: string
	"""

    r = ' '.join(list(map(lambda x: x.swapcase(), string.split())))
    return r


def run():
    """ This function verifies the function flip_case(string)
    with the user, who enters a string. It must be called
    in main. """
    string = input("Enter a string: ")
    print(flip_case(string))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    run()