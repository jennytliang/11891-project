def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: elif a == b :
	"""


    if a > b:
        a, b = b, a

    result = []
    for i in range(a, b + 1, 2):
        if i % 10 == 0 or i % 10 >= 6:
            continue
        result.append(i)

    return result


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))
