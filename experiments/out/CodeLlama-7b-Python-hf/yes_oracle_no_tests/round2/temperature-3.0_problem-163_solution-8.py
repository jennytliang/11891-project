def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: b
	Do not include these tokens in the code: 1 0
	"""


    
    if a > b:
        a, b = b, a
    even_digits = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            even_digits.append(i)
    return even_digits


    # solution 2
    if a > b:
        a, b = b, a
    return [i for i in range(a, b + 1) if i % 2 == 0]


    # solution 3
    return [i for i in range(min(a, b), max(a, b) + 1) if i % 2 == 0]




































































































































































