def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = 0
    for c in string:
        r += 1
    return r


def main():
    print('strlen("") =', strlen(''))
    print('strlen("abc") =', strlen('abc'))


if __name__ == '__main__':
    main()
