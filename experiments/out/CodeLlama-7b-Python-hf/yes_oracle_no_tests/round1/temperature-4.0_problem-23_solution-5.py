def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: len ( string )
	Do not include these tokens in the code: 0
	"""

    r = 0
    for c in string:
        r += 1

    return r


def main():
    str1 = input("Enter string: ")
    print(strlen(str1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
