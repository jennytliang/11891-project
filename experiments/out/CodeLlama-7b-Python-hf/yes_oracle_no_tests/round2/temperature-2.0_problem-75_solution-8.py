def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    prime_list = []
    for i in range(2, a):
        if check_prime(i):
            prime_list.append(i)
    if len(prime_list) < 3:
        return False
    for i in range(0, len(prime_list) - 2):
        for j in range(i + 1, len(prime_list) - 1):
            if prime_list[i] * prime_list[j] * prime_list[j + 1] == a:
                return True
    return False


def check_prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


print(is_multiply_prime(30))
