def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: b
	"""

    if a > 0 and b > 0:
        # YOUR CODE HERE
        pass
    else:
        print("a and b must be positive integers")


if __name__ == '__main__':
    a = int(input("Enter a positive integer: "))
    b = int(input("Enter a positive integer: "))
    generate_integers(a, b)
