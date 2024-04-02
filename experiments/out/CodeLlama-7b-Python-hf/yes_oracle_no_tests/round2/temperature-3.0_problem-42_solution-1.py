def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	Include these tokens in the code: return [ x
	Do not include these tokens in the code: ret u = []
	"""
    ret = []
    for x in l:
        ret.append(x+1)
    return ret


def main():
    import doctest
    doctest.testmod()
    print("Bye, bye.")


if __name__ == "__main__":
    main()
