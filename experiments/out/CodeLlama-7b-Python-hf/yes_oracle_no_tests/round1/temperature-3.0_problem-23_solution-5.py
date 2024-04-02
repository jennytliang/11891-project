def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Do not include these tokens in the code: print ( str len .__ doc __ )
	"""

    return len(stri)


def main():
    """ This function calls strlen() with different arguments
    and prints the returned values.
    """

    str1 = "hello"
    str2 = "world"

    print(str1, strlen(str1), str2, strlen(str2))


if __name__ == "__main__":
    main()
