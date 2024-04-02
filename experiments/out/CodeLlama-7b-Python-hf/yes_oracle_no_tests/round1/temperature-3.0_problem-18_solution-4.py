def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences =
	"""
    return string.count(substring)


def first_is_not_substring(string: str, substring: str) -> bool:
    """ Check if the first character of the string is not a substring of the substring.
    >>> first_is_not_substring('aaa', 'a')
    False
    >>> first_is_not_substring('aabaa', 'aa')
    False
    >>> first_is_not_substring('aabaa', 'b')
    True
    >>> first_is_not_substring('aabaa', 'aaa')
    True
    """
    return string[0] not in substring


def last_is_not_substring(string: str, substring: str) -> bool:
    """ Check if the last character of the string is not a substring of the substring.
    >>> last_is_not_substring('aaa', 'a')
    False
    >>> last_is_not_substring('aabaa', 'aa')
    False
    >>> last_is_not_substring('aabaa', 'b')
    False
    >>> last_is_not_substring('aabaa', 'aaa')
    True
    """
    return string[-1] not in substring


def how_many_times_v2(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times_v2('', 'a')
    0
    >>> how_many_times_v2('aaa', 'a')
    3
    >>> how_many_times_v2('aaaa', 'aa')
    3
    """
    if len(string) == 0 or len(substring) == 0:
        return 0
    if len(string) < len(substring):
        return 0
    if len(string) == len(substring):
        if string == substring:
            return 1
        else:
            return 0

    first_is_not_substring_bool = first_is_not_substring(string, substring)
    last_is