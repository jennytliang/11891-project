def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: # - ---------------- ---------------- ---------------- ----------------
	"""
    # - ---------------- ---------------- ---------------- ---------------- ----------------
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in range(len(primes)):
        if a % primes[i] == 0:
            a = a / primes[i]
        else:
            return False
    return True


def is_multiply_prime2(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: # - ---------------- ---------------- ---------------- ----------------
	"""
    # - ---------------- ---------------- ---------------- ---------------- ----------------
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if a < 100:
        return is_multiply_prime(a)
    else:
        for i in range(len(primes)):
            if a % primes[i] == 0:
                a = a / primes[i]
            else:
                return False
    return True


if __name__ == '__main__':
    print(