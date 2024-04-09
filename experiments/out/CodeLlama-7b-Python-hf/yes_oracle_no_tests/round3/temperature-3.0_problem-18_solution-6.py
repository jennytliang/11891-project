def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences =
	Do not include these tokens in the code: if len ( string ) ==
	"""
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    return count


print(F"how_many_times.py: how_many_times('', 'a') = 0 = {how_many_times('', 'a')}")
print(F"how_many_times.py: how_many_times('aaa', 'a') = 3 = {how_many_times('aaa', 'a')}")
print(F"how_many_times.py: how_many_times('aaaa', 'aa') = 3 = {how_many_times('aaaa', 'aa')}")
