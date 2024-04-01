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


    if 2 > a or 2 > b:
        return []
    else:
        return [x for x in range(a, b + 1) if x % 2 == 0]








generate_integers(2, 8)

generate_integers(8, 2)

generate_integers(10, 14)



























































































































































































































































































































































































































