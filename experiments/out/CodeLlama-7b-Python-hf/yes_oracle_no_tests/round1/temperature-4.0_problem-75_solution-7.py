def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    prime_list = list()
    for i in range(2, a):
        if is_prime(i):
            prime_list.append(i)
    if len(prime_list) < 3:
        return False
    else:
        for i in prime_list:
            for j in prime_list:
                for k in prime_list:
                    if i * j * k == a:
                        return True
        return False


def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


print(is_multiply_prime(30))
print(is_multiply_prime(14))
