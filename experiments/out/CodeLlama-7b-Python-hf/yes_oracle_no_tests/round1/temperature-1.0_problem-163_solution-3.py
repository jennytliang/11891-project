def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: a , b = b , a
	"""

    if a > b:
        return [i for i in range(a, b, 2) if i % 2 ==0]
    elif a == b:
        return []
    else:
        return [i for i in range(a, b, 2) if i % 2 ==0]

    pass