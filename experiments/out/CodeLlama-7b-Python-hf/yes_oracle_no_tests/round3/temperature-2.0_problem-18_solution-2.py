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
    string_length = len(string)
    substring_length = len(substring)
    if substring_length == 0:
        return string_length + 1
    if substring_length > string_length:
        return 0
    counter = 0
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            counter += 1
    return counter


print(f"how_many_times('', 'a') = {how_many_times('', 'a')}")
print(f"how_many_times('aaa', 'a') = {how_many_times('aaa', 'a')}")
print(f"how_many_times('aaaa', 'aa') = {how_many_times('aaaa', 'aa')}")
