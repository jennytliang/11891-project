def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: if len ( substring ) > len
	"""
    if len(string) == 0 or len(substring) == 0:
        return 0
    elif len(substring) > len(string):
        return 0
    else:
        how_many = 0
        for i in range(len(string) - len(substring) + 1):
            if string[i:i + len(substring)] == substring:
                how_many += 1
        return how_many


def how_many_times_with_count(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times_with_count('', 'a')
    0
    >>> how_many_times_with_count('aaa', 'a')
    3
    >>> how_many_times_with_count('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: if len ( substring ) > len
	"""
    if len(string) == 0 or len(substring) == 0:
        return 0
    elif len(substring) > len(string):
        return 0
    else:
        return string.count(substring)


def how_many_times_with_find(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times_with_find('', 'a')
    0
    >>> how_many_times_with_find('aaa', 'a')
    3
    >>> how_many_times_with_find('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: if len ( substring ) > len
	"""
    if len(string) == 0 or len(substring) == 0:
        return 0
    elif len(substring) > len(string):
        return 0
    else:
        how_many