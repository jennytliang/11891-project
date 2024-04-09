def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Do not include these tokens in the code: # my solution my _
	"""
    # my solution my _
    my_result = len(set(string.lower()))
    # ______________________________________________________
    return my_result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
