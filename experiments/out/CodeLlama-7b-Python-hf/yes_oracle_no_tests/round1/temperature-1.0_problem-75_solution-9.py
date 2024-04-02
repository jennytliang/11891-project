def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    if a > 100:
        return False
    
    for i in range(2, a):
        if a % i == 0:
            j = 2
            while j < i:
                if i % j == 0:
                    break
                j += 1
            if j == i:
                return True
    return False

if __name__ == '__main__':
    print(is_multiply_prime(30))
    print(is_multiply_prime(25))
    print(is_multiply_prime(15))
    print(is_multiply_prime(10))
    print(is_multiply_prime(2))
    print(is_multiply_prime(1))
    print(is_multiply_prime(100))
    print(is_multiply_prime(99))
    print(is_multiply_prime(97))
    print(is_multiply_prime(96))
    print(is_multiply_prime(95))
    print(is_multiply_prime(94))
    print(is_multiply_prime(93))
    print(is_multiply_prime(92))
    print(is_multiply_prime(91))
    print(is_multiply_prime(90))
    print(is_multiply_prime(89))
    print(is_multiply_prime(88))
    print(is_multiply_prime(87))
    print(is_multiply_prime(86))
    print(is_multiply_prime(85))
    print(is_multiply_prime(84))
    print(is_multiply_prime(83))
    print(is_multiply_prime(82))
    print(is_multiply_prime(81))
    print(is_multiply_prime(80))
    print(is_multiply_prime(79))
    print(is_multiply_prime(78))
    print(is_multiply_prime(77