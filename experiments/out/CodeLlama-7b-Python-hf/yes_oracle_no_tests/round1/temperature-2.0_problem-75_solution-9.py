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

    if a <= 100:
        i = 2
        while i <= a:
            j = 2
            while j <= a:
                k = 2
                while k <= a:
                    if i * j * k == a:
                        return True
                    k += 1
                j += 1
            i += 1
        return False
    else:
        return False


if __name__ == '__main__':
    print(is_multiply_prime(30))
    print(is_multiply_prime(12))
    print(is_multiply_prime(121))
    print(is_multiply_prime(13))
    print(is_multiply_prime(101))
    print(is_multiply_prime(15))
    print(is_multiply_prime(100))
