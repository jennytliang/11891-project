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
    #pass
    # BEGIN PROBLEM 0
    if a > b:
        return generate_integers(b, a)
    elif a % 2 == 1:
        a += 1
    result = []
    while a <= b:
        if a % 2 == 0:
            result.append(a)
        a += 2
    return result
    # END PROBLEM 0


def generate_floats(a, b):
    """
    Given two positive floating-point numbers a and b, return the even digits
    between a and b, in ascending order.

    For example:
    generate_floats(2.0, 8.0) => [2.0, 4.0, 6.0, 8.0]
    generate_floats(8.0, 2.0) => [2.0, 4.0, 6.0, 8.0]
    generate_floats(10.0, 14.0) => []
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    #pass
    # BEGIN PROBLEM 1
    if a > b:
        return generate_floats(b, a)
    elif a % 2 == 1:
        a += 1
    result = []
    while a <= b:
        if a % 2 == 0:
            result.append(a)
        a += 2
    return result
    # END PROBLEM 1


def generate_strings(a, b):
    """
    Given two strings a and b, return the even digits between a and b, in
    ascending order.

    For example:
    generate_strings('2', '8') => ['2', '4', '6', '8']
    generate_strings('8', '2') => ['2', '4', '6', '8']
    generate_strings('10', '14') => []
    
	Do not include these tokens in the code: #