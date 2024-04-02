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


def how_many_times_with_loop(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times_with_loop('', 'a')
    0
    >>> how_many_times_with_loop('aaa', 'a')
    3
    >>> how_many_times_with_loop('aaaa', 'aa')
    3
    """
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    return count


def how_many_times_with_regex(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times_with_regex('', 'a')
    0
    >>> how_many_times_with_regex('aaa', 'a')
    3
    >>> how_many_times_with_regex('aaaa', 'aa')
    3
    """
    import re
    return len(re.findall(substring, string))


def how_many_times_with_regex_2(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times_with_regex_2('', 'a')
    0
    >>> how_many_times_with_regex_2('aaa', 'a')
    3
    >>> how_many_times_with_regex_2('aaaa', 'aa')
    3
    """
    import re
    return len(re.findall(f"(?={substring})", string))


def how_many_times_with_regex_3(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times_with_