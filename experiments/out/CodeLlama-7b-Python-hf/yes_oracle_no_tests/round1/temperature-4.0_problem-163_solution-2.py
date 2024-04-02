def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: if a > b : a
	Do not include these tokens in the code: # base case
	"""
    if a > b:
        a, b = b, a
    return [i for i in range(a, b + 1) if i % 2 == 0]


# Pybites solution


def generate_integers1(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    return [i for i in range(min(a, b), max(a, b) + 1, 2) if i % 2 == 0]
