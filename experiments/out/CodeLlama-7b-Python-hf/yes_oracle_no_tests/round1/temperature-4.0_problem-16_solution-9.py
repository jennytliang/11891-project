def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Include these tokens in the code: return len ( set ( string . lower ()))
	"""
    return len(set(string.lower()))


def count_distinct_characters_with_setdefault(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters_with_setdefault('xyzXYZ')
    3
    >>> count_distinct_characters_with_setdefault('Jerry')
    4
    
	Include these tokens in the code: return len ( string . lower (). setdefault ())
    """
    distinct = {}
    for c in string.lower():
        distinct.setdefault(c, 0)
    return len(distinct)


def count_distinct_characters_with_dict(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters_with_dict('xyzXYZ')
    3
    >>> count_distinct_characters_with_dict('Jerry')
    4
    
	Include these tokens in the code: return len ( string . lower (). keys ())
    """
    return len(string.lower().keys())


def count_distinct_characters_with_defaultdict(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters_with_defaultdict('xyzXYZ')
    3
    >>> count_distinct_characters_with_defaultdict('Jerry')
    4
    
	Include these tokens in the code: return len ( string . lower (). defaultdict ())
    """
    from collections import defaultdict

    distinct = defaultdict(int)
    for c in string.lower():
        distinct[c] += 1
    return len(distinct)


def count_distinct_characters_with_counter(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist