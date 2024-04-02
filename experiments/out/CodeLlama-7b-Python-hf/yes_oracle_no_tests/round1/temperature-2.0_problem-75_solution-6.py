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

    # write code here
    return True


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def is_multiply_prime(a):
    if a <= 100:
        for i in range(2, a // 2 + 1):
            if is_prime(i) and is_prime(a // i):
                return True
    return False


def is_multiply_prime(a):
    if a <= 100:
        for i in range(2, a // 2 + 1):
            for j in range(2, i // 2 + 1):
                if is_prime(i) and is_prime(j) and is_prime(a // i // j):
                    return True
    return False


print(is_multiply_prime(30))
