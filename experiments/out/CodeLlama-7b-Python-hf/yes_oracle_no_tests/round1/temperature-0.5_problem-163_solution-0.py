def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: a , b = b
	Do not include these tokens in the code:  return generate _ inte gers (
	"""

    if a > b:
 
        return generate_integers(b, a)
    elif (a % 2 != 0) or (b % 2 != 0):
        return []
    elif a > b:
        return []
    elif a == b:
        return [a]
    else:
        return [a, b]


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))
print(generate_integers(8, 8))
print(generate_integers(10, 10))
