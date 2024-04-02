def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Include these tokens in the code: ()))
	Do not include these tokens in the code: ( ))) def count _ dist
	"""


    return len(set(string.lower())) if string else 0


