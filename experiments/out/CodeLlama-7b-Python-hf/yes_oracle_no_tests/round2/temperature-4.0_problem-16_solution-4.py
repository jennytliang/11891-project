def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Do not include these tokens in the code: ret ur nt ype = int
	"""
    # BEGIN PROBLEM 1
    return len(set(string))
    # END PROBLEM 1


def count_distinct_words(string: str) -> int:
    """ Given a string, find out how many distinct words (regardless of case) does it consist of
    >>> count_distinct_words('xyz xyz XYZ')
    2
    >>> count_distinct_words('Jerry Jerry Jerry')
    1
    
	Do not include these tokens in the code: ret ur nt ype = int
	"""
    # BEGIN PROBLEM 2
    return len(set(string.split()))
    # END PROBLEM 2


def count_matching_characters(string_1: str, string_2: str) -> int:
    """ Given two strings, find out how many characters from the first string are present in the second
    string, without regard to case.
    >>> count_matching_characters('xyz', 'XYZ')
    3
    >>> count_matching_characters('Jerry', 'Jerry')
    4
    
	Do not include these tokens in the code: ret ur nt ype = int
	"""
    # BEGIN PROBLEM 3
    count = 0
    for char in string_1:
        if char.lower() in [i.lower() for i in string_2]:
            count += 1
    return count
    # END PROBLEM 3


def count_matching_words(string_1: str, string_2: str) -> int:
    """ Given two strings, find out how many words from the first string are present in the second
    string, without regard to case.
    >>> count_matching_words('xyz xyz', 'XYZ')
    2
    >>> count_matching_words('Jerry Jerry Jerry', 'Jerry')
    3
    
	Do not include these tokens in the code: ret ur nt ype = int
	"""
    # BEGIN PROBLEM 4
    count = 0
    for