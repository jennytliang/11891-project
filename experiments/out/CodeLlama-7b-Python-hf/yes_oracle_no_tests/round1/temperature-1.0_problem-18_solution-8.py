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
    start_idx = 0
    occurence_count = 0

    while True:
        found_idx = string.find(substring, start_idx)
        # check that no more substring are to come
        if found_idx == -1:
            # print(f"Occurences: {occurence_count}")
            return occurence_count
        # print(found_idx)
        occurence_count += 1
        start_idx = found_idx + 1


print(how_many_times("abaababa", "a"))
