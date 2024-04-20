def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: =
	"""



    if a > 9 or b > 9 or a < 0 or b < 0:
        raise ValueError('The number must be between 0 and 9.')

    if a > b:
        a, b = b, a

    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)
    
    return result


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))