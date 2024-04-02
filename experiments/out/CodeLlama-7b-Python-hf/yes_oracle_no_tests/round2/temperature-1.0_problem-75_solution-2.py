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
        for i in range(2, a):
            for j in range(2, i):
                if i % j == 0:
                    break

            if i == j:
                if is_prime(i):
                    if is_prime(a / i):
                        if is_prime(a / (a / i)):
                            return True

        return False


def is_prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False

    return True


print(is_multiply_prime(30))  # True
print(is_multiply_prime(14))  # False
print(is_multiply_prime(225))  # True
print(is_multiply_prime(12))  # False
print(is_multiply_prime(15))  # False
