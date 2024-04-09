def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: 9 and b > 9 and a <
	"""

    i = a
    if a > b:
        i = b
    else:
        i = a
    result = []
    while i <= b:
        if i % 2 == 0:
            result.append(i)
        i += 1
    return result


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))
