def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: count
	"""
    count = 0
    for i in range(len(string)):
        index = string.find(substring, i)
        if index != -1:
            count += 1
    return count


if __name__ == "__main__":
    how_many_times("aaa", "a")
