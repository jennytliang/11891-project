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
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for i in prime_numbers:
            if a == 1:
                return False
            while a % i == 0:
                a = a / i
                if a == 1:
                    return True
    return False

if __name__ == '__main__':
    print(is_multiply_prime(30))
    print(is_multiply_prime(17))
    print(is_multiply_prime(100))
    print(is_multiply_prime(5))






















