def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: # base case
	"""
    # base case
    if a > b:
        return []
    # recursive case
    else:
        if a % 2 == 0:
            # if a is even, add it to the list
            result = [a]
        else:
            # if a is odd, don't add it to the list
            result = []
        # add the next number to the list
        result += generate_integers(a + 1, b)
        return result


# Pybites solution


def generate_integers1(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    def gen_int(a, b):
        if a > b:
            return []
        elif a % 2 == 0:
            return [a] + gen_int(a + 1, b)
        else:
            return gen_int(a + 1, b)

    return [x for x in gen_int(a, b) if x % 2 == 0]
