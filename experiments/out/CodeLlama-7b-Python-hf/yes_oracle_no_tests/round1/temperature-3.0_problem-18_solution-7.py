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
    count = 0
    for char in range(len(string)):
        if string[char] == substring[0]:
            for sub_char in range(len(substring)):
                if string[char + sub_char] == substring[sub_char]:
                    count += 1
                else:
                    break
                if sub_char == len(substring) - 1:
                    count += 1
    return count


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
    count = 0
    for char in range(len(string)):
        if string[char] == substring[0]:
            for sub_char in range(len(substring)):
                if string[char + sub_char] == substring[sub_char]:
                    count += 1
                else:
                    break
                if sub_char == len(substring) - 1:
                    count += 1
    return count


def how_many_times_v3(string: str, substring: str) -> int:
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # print(how_many_times('', 'a'))
    # print(how_many_times('aa