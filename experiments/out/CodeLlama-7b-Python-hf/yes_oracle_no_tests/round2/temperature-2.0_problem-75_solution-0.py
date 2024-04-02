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
        if is_prime(i):
            prime_list.append(i)
    if len(prime_list) < 3:
        return False
    prime_list = prime_list[:3]
    for i in range(len(prime_list)):
        for j in range(i + 1, len(prime_list)):
            if prime_list[i] * prime_list[j] == a:
                return True
    return False

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True













