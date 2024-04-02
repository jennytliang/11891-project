def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: pass def generate _
	"""
    # YOUR CODE HERE
    if a > b:
        a, b = b, a
    return [x for x in range(a, b+1) if x % 2 == 0]


if __name__ == '__main__':
    print("Example:")
    print(list(generate_integers(2, 8)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(generate_integers(2, 8)) == [2, 4, 6, 8]
    assert list(generate_integers(8, 2)) == [2, 4, 6, 8]
    assert list(generate_integers(10, 14)) == []
    assert list(generate_integers(20, 28)) == [22, 24, 26, 28]
    print("Coding complete? Click 'Check' to earn cool rewards!")
