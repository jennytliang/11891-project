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
    # Generate the even numbers between a and b
    even_integers = [i for i in range(a, b + 1) if i % 2 == 0]
    
    # Sort the even numbers
    even_integers.sort()
    
    return even_integers


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))