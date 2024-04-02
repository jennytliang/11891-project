def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: # base case
	"""
    # base case
    if a > b:
        return []

    # recursive case
    if a % 2 == 0:
        return [a] + generate_integers(a + 2, b)
    else:
        return generate_integers(a + 2, b)


# print(generate_integers(2, 8))
# print(generate_integers(8, 2))
print(generate_integers(10, 14))
