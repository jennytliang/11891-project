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

    if a > b:
        a, b = b, a
    b -= 1
    while a < b:
        if a %2 == 0:
          print(a , end = '')
        a += 1
    if b %2 == 0:
          print(b , end = '')


#Pybites solution


def generate_integers(a, b):
    if a > b: a, b = b, a
    return filter(lambda i: not i%2, range(a, b+1))
