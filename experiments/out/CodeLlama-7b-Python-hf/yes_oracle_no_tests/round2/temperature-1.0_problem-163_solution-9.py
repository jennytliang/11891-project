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
    # your code here
    if a > b:
        a, b = b, a
    list = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            list.append(i)
    return list


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))
print(generate_integers(1, 4))
print(generate_integers(10, 20))
print(generate_integers(20, 10))
