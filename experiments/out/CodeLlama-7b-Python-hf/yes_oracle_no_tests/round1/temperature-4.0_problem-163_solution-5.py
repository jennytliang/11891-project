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
    pass


def generate_integers(a, b):
    if a > b:
        return []
    elif a % 2 == 0:
        return [a] + generate_integers(a + 2, b)
    else:
        return generate_integers(a + 2, b)


def generate_integers(a, b):
    if a > b:
        return []
    else:
        return [a] + generate_integers(a + 2, b) if a % 2 == 0 else generate_integers(a + 2, b)


def generate_integers(a, b):
    if a > b:
        return []
    else:
        return [a] + generate_integers(a + 2, b) if a % 2 == 0 else generate_integers(a + 2, b)
