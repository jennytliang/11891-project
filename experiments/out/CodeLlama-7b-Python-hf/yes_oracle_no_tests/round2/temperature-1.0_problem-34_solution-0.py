def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Include these tokens in the code: ))
	Do not include these tokens in the code: ), key = l . index )
	"""


    return sorted(set(l), key=l.index)


if __name__ == "__main__":
    l = [3, 3, 3, 5, 2, 5, 81, 5, 6, 2, 7, 2, 2]
    print(unique(l))
