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


def main():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('aaaa', 'aaa') == 2
    assert how_many_times('aaaa', 'aaaa') == 1
    assert how_many_times('aaaa', 'a') == 0
    assert how_many_times('aaaa', 'b') == 0
    assert how_many_times('abcab', 'abc') == 2
    assert how_many_times('aaaaa', 'aaa') == 3
    assert how_many_times('aaaaa', 'aa') == 2


if __name__ == "__main__":
    main()