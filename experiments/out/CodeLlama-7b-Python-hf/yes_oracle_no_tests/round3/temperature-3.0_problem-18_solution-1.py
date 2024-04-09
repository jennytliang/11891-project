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
    substring_length = len(substring)
    string_length = len(string)
    if substring_length == 0:
        return 0
    if string_length == 0:
        return 0
    if substring_length > string_length:
        return 0
    occurences = 0
    for i in range(0, string_length - substring_length + 1):
        if string[i:i + substring_length] == substring:
            occurences += 1
    return occurences


def how_many_times_no_slices(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
    """
    substring_length = len(substring)
    string_length = len(string)
    if substring_length == 0:
        return 0
    if string_length == 0:
        return 0
    if substring_length > string_length:
        return 0
    occurences = 0
    for i in range(0, string_length - substring_length + 1):
        for j in range(0, substring_length):
            if string[i + j] != substring[j]:
                break
        if j == substring_length - 1:
            occurences += 1
    return occurences


def main():
    import doctest
    doctest.testmod()
    string = input('Enter a string: ')
    substring = input('Enter a substring: ')
    result = how_many_times(string, substring)
    print(result)


if __name__ == '__main__':
    main()
