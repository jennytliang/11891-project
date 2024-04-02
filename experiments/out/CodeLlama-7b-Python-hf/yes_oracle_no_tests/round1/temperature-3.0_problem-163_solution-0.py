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
        a = a % 10
    if b > 10:
        b = b % 10
    if b < a:
        a, b = b, a
    res = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            res.append(i)
    return res


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))
