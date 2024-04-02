def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Do not include these tokens in the code: if __ name __ == " __ main __ ":
	"""

    return len(set(string.lower(string)))


if __name__ == "__main__":
    print("Example:")
    print(count_distinct_characters('abc'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('aabBcde') == 4
    assert count_distinct_characters('Indivisibility') == 7
    assert count_distinct_characters('a') == 1
    assert count_distinct_characters('AAA') == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
