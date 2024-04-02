def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: 0 0
	"""

    if a < 100:
        i = 2
        while i < a:
            if a % i == 0:
                j = 2
                while j < i:
                    if i % j == 0:
                        k = 2
                        while k < j:
                            if j % k == 0:
                                return True
                            k += 1
                    j += 1
            i += 1
    return False


print(is_multiply_prime(30))
