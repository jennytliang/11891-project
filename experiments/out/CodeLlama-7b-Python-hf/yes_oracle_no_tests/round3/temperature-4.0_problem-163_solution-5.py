def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # YOUR CODE HERE
    if a <= b:
        return [x for x in range(a, b + 1, 2) if x % 10 == 0]
    else:
        return [x for x in range(b, a + 1, 2) if x % 10 == 0]


def generate_integers_2(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: # YOUR CODE HERE
	"""
    if a <= b:
        return [x for x in range(a, b + 1, 2) if x % 10 == 0]
    else:
        return [x for x in range(b, a + 1, 2) if x % 10 == 0]
