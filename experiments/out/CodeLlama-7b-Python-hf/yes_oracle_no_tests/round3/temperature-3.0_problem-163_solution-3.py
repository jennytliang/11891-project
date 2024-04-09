def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: if a > b : a , b = b
	"""
    # YOUR CODE HERE
    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b+1):
        if i % 2 == 0:
            result.append(i)
    return result


def generate_floats(a, b, c):
    """
    Given three positive integers a, b and c, return the floats between a
    and b, in ascending order, with a precision of c digits after the decimal
    point.

    For example:
    generate_floats(1, 10, 2) => [1.00, 1.01, 1.02, 1.03, 1.04, ..., 9.97, 9.98, 9.99, 10.00]
    generate_floats(10, 20, 3) => [10.000, 10.001, 10.002, ..., 19.997, 19.998, 19.999]
    generate_floats(100, 200, 0) => [100.0, 101.0, 102.0, ..., 198.0, 199.0, 200.0]
    
	Include these tokens in the code: if a > b : a , b = b
	"""
    # YOUR CODE HERE
    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b+1):
        for j in range(10**(c-1), 10):
            result.append(float(str(i) + '.' + str(j)))
    return result


def generate_strings(a, b):
    """
    Given two positive integers a and b, return the strings between a
    and b, in ascending order.

    For example:
    generate