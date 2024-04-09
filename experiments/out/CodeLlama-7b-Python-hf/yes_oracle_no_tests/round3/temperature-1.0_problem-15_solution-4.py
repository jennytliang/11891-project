def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Do not include these tokens in the code: # BEGIN _ S OL UT ION
	"""

    # BEGIN SOLUTION
    return " ".join(str(i) for i in range(n + 1))
    # END SOLUTION


if __name__ == "__main__":
    print("Example:")
    print(string_sequence(1))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert string_sequence(0) == "0"
    assert string_sequence(1) == "0 1"
    assert string_sequence(2) == "0 1 2"
    assert string_sequence(3) == "0 1 2 3"
    assert string_sequence(4) == "0 1 2 3 4"
    assert string_sequence(5) == "0 1 2 3 4 5"
    print("Coding complete? Click 'Check' to earn cool rewards!")
