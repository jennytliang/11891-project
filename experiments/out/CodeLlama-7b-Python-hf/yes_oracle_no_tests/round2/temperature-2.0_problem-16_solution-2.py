def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Include these tokens in the code: ()))
	Do not include these tokens in the code: ( string )))
	"""


    return len(set(string.lower()))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
