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
        primes = []
        for i in range(2, a):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
        if len(primes) < 3:
            return False
        return a == primes[0] * primes[1] * primes[2]