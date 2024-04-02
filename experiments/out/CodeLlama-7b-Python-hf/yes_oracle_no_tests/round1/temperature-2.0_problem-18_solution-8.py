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
    occurences = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            occurences += 1
    return occurences


def how_many_times_v2(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences =
	"""
    occurences = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            occurences += 1
    return occurences


def main():
    print(how_many_times_v2('aaaa', 'aa'))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
