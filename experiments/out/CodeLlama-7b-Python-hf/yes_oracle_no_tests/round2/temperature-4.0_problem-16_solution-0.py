def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Include these tokens in the code: return len ( set ( string . lower ()))
	"""
    return len(set(string.lower()))


def count_distinct_characters2(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Include these tokens in the code: return len ( set ( string . lower ()))
	"""
    return len({char.lower() for char in string})


def main():
    print(count_distinct_characters('xyzXYZ'))
    print(count_distinct_characters('Jerry'))
    print(count_distinct_characters('Jerry'))


if __name__ == '__main__':
    main()
