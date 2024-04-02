def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Do not include these tokens in the code: unique ([ 5 , 3 , 5 , 2 ,
	"""


    return sorted(set(l))

def max_index(l: list):
    """Return the index of the max element in l
    >>> max_index([0, 1, 4, 10])
    2
    >>> max_index ([3, 3, 4, 3, 4, 0, 0, 2])
    5
    """
    
    return len(l) - 1 - l[::-1].index(max(l))
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)