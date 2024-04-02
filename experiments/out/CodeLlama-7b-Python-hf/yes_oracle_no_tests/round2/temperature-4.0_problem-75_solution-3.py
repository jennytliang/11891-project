def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    # my solution
    # def is_multiply_prime(a):
    #     prime_count = 0
    #     for i in range(2, a):
    #         if a % i == 0:
    #             prime_count += 1
    #     if prime_count == 2:
    #         return True
    #     return False

    # better solution
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_multiply_prime(a):
        prime_count = 0
        for i in range(2, a):
            if a % i == 0:
                prime_count += 1
        if prime_count == 3:
            return True
        return False

    # for i in range(2, a):
    #     if a % i == 0:
    #         prime_count += 1
    # if prime_count == 3:
    #     return True
    # return False


print(is_multiply_prime(30))
print(is_multiply_prime(12))
print(is_multiply_prime(3))
print(is_multiply_prime(11))
print(is_multiply_prime(24))
