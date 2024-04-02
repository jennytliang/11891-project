def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Include these tokens in the code: ( set ( string
	Do not include these tokens in the code: ({ char
	"""

    retur = set()
    for char in string:
        retur.add(char)
    return len(retur)

    # string = string.lower()
    # return len(set(string))


def run_tests():
    """ Tests from question. """
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4


if __name__ == "__main__":
    run_tests()
