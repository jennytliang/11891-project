def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: >
	"""

    # WRITE YOUR CODE HERE
    i = 2
    j = 0
    while i <= 100:
        k = 2
        while k <= 100:
            if i * j * k == a:
                return True
            k += 1
        j += 1
        i += 1

    return False


print(is_multiply_prime(30))
