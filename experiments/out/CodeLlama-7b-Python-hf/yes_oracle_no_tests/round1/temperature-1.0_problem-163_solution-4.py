def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: a , b = b
	Do not include these tokens in the code: return generate _ inte gers (
	"""

    if a < b:
        print(a)
        for x in range(a+2, b+1, 2):
            print(x)
    else:
        print(a)
        for x in range(a+2, b+1, 2):
            print(x)


if __name__ == "__main__":
    generate_integers(2, 8)
    generate_integers(8, 2)
    generate_integers(10, 14)