def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Do not include these tokens in the code: ret ur nd ict = {}
	"""
    # my solution
    my_dict = {}
    for i in string:
        if i.lower() not in my_dict:
            my_dict[i.lower()] = 1
        else:
            my_dict[i.lower()] += 1
    return len(my_dict)


def count_distinct_characters2(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
	Do not include these tokens in the code: ret ur nd ict = {}
	"""
    # solution 2
    return len({i: 1 for i in string}.keys())


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print("Example:")
    print(count_distinct_characters("xyzXYZ"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_distinct_characters("xyzXYZ") == 3, "Example"
    assert count_distinct_characters("Jerry") == 4, "Example"
    assert count_distinct_characters("alphabet") == 5, "Repetition"
    assert count_distinct_characters("JESSE") == 4, "JESSE"
    assert count_distinct_characters("") == 0, "Empty"
    print("Coding complete? Click 'Check' to earn cool rewards!")
