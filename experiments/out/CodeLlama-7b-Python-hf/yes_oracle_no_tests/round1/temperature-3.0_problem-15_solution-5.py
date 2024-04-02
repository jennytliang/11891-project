def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Do not include these tokens in the code: # solution target
	"""
    # write code here
    return " ".join(str(i) for i in range(n + 1))


if __name__ == "__main__":
    print("Example:")
    print(string_sequence(5))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert string_sequence(5) == "0 1 2 3 4 5"
    assert string_sequence(1) == "0"
    assert string_sequence(3) == "0 1 2 3"
    print("Coding complete? Click 'Check' to earn cool rewards!")
