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
    num_substrings = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i : i + len(substring)] == substring:
            num_substrings += 1

    return num_substrings
""" if num_substrings >= 1:
    occur = "occur"
    ences = "ences "

else:
    occur = "occur"
    ences = "ence " """


if __name__ == "__main__":
    str_count = input("String: ").strip()
    substring_count = input("Substring: ").strip()

    how_many = how_many_times(str_count, substring_count)
    print(f"{str_count} has {how_many} " + occur + ences + str(substring_count))
