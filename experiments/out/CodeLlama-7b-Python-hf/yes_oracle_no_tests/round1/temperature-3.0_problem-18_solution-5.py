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
    print(f"{' Do not modify this function! ':=^80}")
    print(f"{'':-^80}")
    print(f"{'how_many_times function:':^80}")
    print(f"{'':-^80}")
    how_many_times('', 'a')
    how_many_times('aaa', 'a')
    how_many_times('aaaa', 'aa')
    print(f"{'':-^80}")


if __name__ == '__main__':
    main()
