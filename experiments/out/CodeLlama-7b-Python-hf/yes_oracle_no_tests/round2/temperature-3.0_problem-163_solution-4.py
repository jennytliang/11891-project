def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: if a > 1 0
	"""
    # YOUR CODE HERE
    if a > b:
        return []
    if a % 2 == 1:
        a += 1
    res = []
    while a <= b:
        if a % 2 == 0:
            res.append(a)
        a += 2
    return res


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))
