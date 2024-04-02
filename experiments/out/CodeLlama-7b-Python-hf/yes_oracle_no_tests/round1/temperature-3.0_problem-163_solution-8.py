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

    if a > 10:
        a = int(a / 10) * 10

    if b > 10:
        b = int(b / 10) * 10

    if b < a:
        a, b = b, a

    return [x for x in range(a, b + 1, 2) if a <= x <= b]





