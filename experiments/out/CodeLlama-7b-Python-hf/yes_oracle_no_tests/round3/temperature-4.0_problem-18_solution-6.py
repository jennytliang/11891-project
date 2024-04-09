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
    for _ in range(len(string) - len(substring) + 1):
        if string[0: len(substring)] == substring:
            occurences += 1
            string = string[1:]
    return occurences

print(how_many_times('', 'a'))
print(how_many_times('aaa', 'a'))
print(how_many_times('aaaa', 'aa'))