def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: return [ i for i in range ( a ,
	Do not include these tokens in the code: c =
	"""


    if a > b:
        a, b = b, a

    def make_digits(int: int) -> list:
        count = "0123456789"
        string = str(int)
        out = []

        for c in string:
            if c in count:
                out.append(int(c))

        return out

    return [ i for i in range(a, b+1) if not (i - make_digits(i)[0]) % 2 ]


    """return None"""


    """return[i for i in range(a,b+1)]"""

    """list =[]
    for i in range(a,b+1):
        list.append(i)




    return[i for i in list if not len(str(i))%2]"""

    """
   x = [2*i for i in range(1, n//2 + 1)][1::2]
    """

    """return [ i for i in range(a, b+1)"""
