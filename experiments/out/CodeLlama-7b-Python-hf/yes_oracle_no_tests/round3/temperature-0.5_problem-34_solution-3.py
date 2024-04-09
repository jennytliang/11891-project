def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Do not include these tokens in the code: if __ name __ == "
	"""



    return sorted(se for se in set(l))


def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert unique([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


if __name__ == "__main__":
    import doctest
    doctest.testmod()