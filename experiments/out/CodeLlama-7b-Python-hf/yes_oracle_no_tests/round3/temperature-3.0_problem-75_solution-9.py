def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    pass


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def is_multiply_prime_alt(a):
    if a <= 100:
        count = 0
        for i in range(2, a):
            if is_prime(i):
                count += 1
            if count == 3:
                return True
    return False


def is_multiply_prime_alt_2(a):
    if a <= 100:
        count = 0
        for i in range(2, a):
            if is_prime(i):
                count += 1
            if count == 3:
                return True
    return False


def main():
    a = 30
    print(is_multiply_prime(a))
    print(is_multiply_prime_alt(a))
    print(is_multiply_prime_alt_2(a))


if __name__ == '__main__':
    main()
