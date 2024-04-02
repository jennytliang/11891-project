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
    string = string.lower()
    substring = substring.lower()
    number_of_occurences = 0
    length_of_substring = len(substring)
    for i in range(len(string) - length_of_substring + 1):
        substring_i = string[i : i + length_of_substring]
        if substring == substring_i:
            number_of_occurences += 1
    return number_of_occurences
