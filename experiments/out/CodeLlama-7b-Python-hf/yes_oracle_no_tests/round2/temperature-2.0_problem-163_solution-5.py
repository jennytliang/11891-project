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
        return generate_integers(b, a)
    if a % 2 == 0 and b % 2 == 1:
        return generate_integers(a, a + 2)
    if a % 2 == 0 and b % 2 == 0:
        return generate_integers(a, b)
    if a % 2 == 1 and b % 2 == 1:
        return generate_integers(a + 2, b)
    if a % 2 == 1 and b % 2 == 0:
        return generate_integers(a + 2, b - 2)
    return []


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))