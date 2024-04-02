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

    divisors = []

    for i in range(1, a):
        if a % i == 0:
            divisors.append(i)

    if len(divisors) != 3:
        return False

    for i in divisors:
        if not is_prime(i):
            return False

    return True


def is_prime(a):
    "Write a function that returns true if the given number is prime and false otherwise."
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


if __name__ == '__main__':
    num = 30
    print(is_multiply_prime(num))
