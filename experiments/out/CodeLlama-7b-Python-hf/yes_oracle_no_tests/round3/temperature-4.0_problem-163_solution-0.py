def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: i
	Do not include these tokens in the code: int ( x )
	"""

    if a > b:
        a, b = b, a
    integers = []
    i = a
    while i <= b:
        if i % 2 == 0:
            integers.append(i)
        i += 1
    return integers

print(generate_integers(2,8))
print(generate_integers(8,2))
print(generate_integers(10,14))
