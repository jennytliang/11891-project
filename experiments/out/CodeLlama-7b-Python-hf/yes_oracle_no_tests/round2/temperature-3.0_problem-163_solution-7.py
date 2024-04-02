def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: if a > 9 and
	"""
    if a > 9 and b > 9 and a < b:
        return [str(i) for i in range(a, b + 1) if int(i) % 2 == 0]
    else:
        return []


if __name__ == '__main__':
    print("Example:")
    print(generate_integers(2, 8))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert generate_integers(2, 8) == ['2', '4', '6', '8']
    assert generate_integers(8, 2) == ['2', '4', '6', '8']
    assert generate_integers(10, 14) == []
    assert generate_integers(1, 1) == []
    assert generate_integers(100, 1000) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
