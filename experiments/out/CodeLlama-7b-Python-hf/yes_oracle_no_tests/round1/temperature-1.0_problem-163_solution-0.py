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
    c = 2
    while a < b and len(list(str(c)))%2 == 0:
        a += 1
        if a > b:
            break
        if len(list(str(a)))%2 == 0:
            print(a)
        elif a == b:
            break
        if len(list(str(b)))%2 == 0:
            print(b)
        else:
            break
             

    print(a, b)
                 
generate_integers(3,8)
generate_integers(4,8)
generate_integers(1,999) 