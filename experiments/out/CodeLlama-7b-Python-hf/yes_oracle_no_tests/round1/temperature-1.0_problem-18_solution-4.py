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
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count


print(f'Result: {how_many_times("aaa", "a")}')
print(f'Result: {how_many_times("aaa", "aa")}')
print(f'Result: {how_many_times("", "a")}')
print(f'Result: {how_many_times("aaaa", "aa")}')
print(f'Result: {how_many_times("aaaaa", "aa")}')
print(f'Result: {how_many_times("aaaa", "aaa")}')
print(f'Result: {how_many_times("aaaa", "aaaa")}')
print(f'Result: {how_many_times("aaaa", "aaaaa")}')
print(f'Result: {how_many_times("aaaa", "a")}')
print(f'Result: {how_many_times("aaaa", "aa")}')
print(f'Result: {how_many_times("aaaa", "aaa")}')
print(f'Result: {how_many_times("aaaa", "aaaa")}')
print(f'Result: {how_many_times("aaaa", "aaaaa")}')
