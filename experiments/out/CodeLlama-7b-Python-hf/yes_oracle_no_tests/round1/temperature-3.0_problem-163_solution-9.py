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

    if a > 0 and b > 0:
        if a > b:
            a, b = b, a
        for i in range(a, b+1):
            if i % 2 == 0:
                print(i, end=' ')


if __name__ == '__main__':
    generate_integers(2, 8)
