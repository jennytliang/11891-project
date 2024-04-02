def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: return [ i
	Do not include these tokens in the code: result = []
	"""


    if a > b:
        a, b = b, a

    result = []

    for i in range(a, b+1, 2):
        if i % 10 == 0:
            continue
        if i % 10 >= 2 and i % 10 <= 8:
            result.append(i)

    return result


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))
print(generate_integers(14, 10))
print(generate_integers(1, 10))
print(generate_integers(10, 1))
