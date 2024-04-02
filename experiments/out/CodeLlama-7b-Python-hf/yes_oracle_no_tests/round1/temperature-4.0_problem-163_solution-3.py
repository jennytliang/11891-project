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
        return generate_integers(b, a)
    if a % 2 != 0:
        a += 1
    if a > b:
        return []
    elif a == b:
        return [a]
    else:
        return [a] + generate_integers(a + 2, b)


def generate_integers_recursive(a, b):
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
        return generate_integers_recursive(b, a)
    if a % 2 != 0:
        a += 1
    if a > b:
        return []
    elif a == b:
        return [a]
    else:
        return [a] + generate_integers_recursive(a + 2, b)


def generate_integers_recursive_2(a, b):
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
        return generate_integers_recursive_2(b, a)
