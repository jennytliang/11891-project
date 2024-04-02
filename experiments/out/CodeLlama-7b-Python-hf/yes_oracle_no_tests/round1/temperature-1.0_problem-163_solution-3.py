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
        a, b = b, a
    elif a == b:
        return [a]

    return [x for x in range(a, b + 1, 2) if x % 10 == 0 or x % 10 == 2 or x % 10 == 4 or x % 10 == 6 or x % 10 == 8]


if __name__ == '__main__':
    print generate_integers(2, 8)
    print generate_integers(8, 2)
    print generate_integers(10, 14)