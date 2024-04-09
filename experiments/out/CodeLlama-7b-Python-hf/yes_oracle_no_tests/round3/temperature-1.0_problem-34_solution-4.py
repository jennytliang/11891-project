def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Include these tokens in the code: set
	Do not include these tokens in the code: se for se in
	"""



    return 


def main():
    """Tests unique function"""
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    assert unique([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert unique([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1]
    assert unique([1, 2, 3]) == [1, 2, 3]
    assert unique([1, 1, 1, 2, 2, 2, 3, 3, 3]) == [1, 2, 3]
    assert unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert unique([]) == []
    assert unique([1]) == [1]
    assert unique([1, 1]) == [1]
    assert unique([5, 5, 5, 5]) == [5]
    assert unique([5, 5, 5, 5, 5]) == [5]
    assert unique([5, 5, 5, 5, 5, 5]) == [5]
    assert unique([5, 5, 5, 5, 5, 5, 5]) == [5]
    assert unique([5, 5, 5, 5, 5,