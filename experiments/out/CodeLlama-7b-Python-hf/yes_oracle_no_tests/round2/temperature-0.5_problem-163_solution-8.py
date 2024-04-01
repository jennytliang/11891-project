def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: a , b = b , a
	"""


    if  a >= b:
        return []
    else:
        if a % 2 == 0:
            even_list = [a]
        else:
            even_list = []
        while a < b:
            a += 2
            if a <= b:
                even_list.append(a)
        return even_list




print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))