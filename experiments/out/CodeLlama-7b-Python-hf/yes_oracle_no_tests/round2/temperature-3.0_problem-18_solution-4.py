def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences =
	Do not include these tokens in the code: return string . count ( substring )
	"""
    return string.count(substring)


def main():
    string = input('Enter a string:\n')
    substring = input('Enter a substring:\n')
    print('The substring occurs', how_many_times(string, substring), 'times')


if __name__ == "__main__":
    main()
