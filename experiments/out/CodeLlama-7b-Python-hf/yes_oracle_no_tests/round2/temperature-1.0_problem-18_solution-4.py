def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: num _ sub strings
	"""
    n_occur_ences = 0
    num_sub_strings = 0
    if len(substring) > len(string):
        return n_occur_ences
    for i in range(0, len(string) - len(substring) + 1):
        temp_sub = string[i:i + len(substring)]
        if temp_sub == substring:
            n_occur_ences += 1
        num_sub_strings += 1
    return float(n_occur_ences)/num_sub_strings

if __name__ == '__main__':
    how_many_times('', 'a')