def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: b
	"""

    if a > 9 and b < 10:
        return []

    if a > b:
        return []

    if a < 10 and b < 10:
        if (a % 2 == 0 and b % 2 == 0):
            return [a, b]
        elif a % 2 == 0:
            return [a]
        elif b % 2 == 0:
            return [b]
        else:
            return []

    if a < 10 and b > 9:
        if (a % 2 == 0 and b % 2 == 0):
            return [a]
        elif a % 2 == 0:
            return [a]
        else:
            return []

    if a > 9 and b > 9:
        if (a % 2 == 0 and b % 2 == 0):
            return [a, b]
        elif a % 2 == 0:
            return [a]
        elif b % 2 == 0:
            return [b]
        else:
            return []

    return []










































































































































































































































