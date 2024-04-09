def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: 0 <=
	"""


    # Generate list of integers from a to b
    integers = range(a, b + 1)

    # Filter out odd and even integers
    integers = filter(lambda x: x % 2 == 0, integers)

    return integers

print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))
