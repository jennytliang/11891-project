def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


    return ma(l)


def ma(l):
    maxi = l[0]
    for i in l:
        if i > maxi:
            maxi = i
    return maxi


def main():
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
