def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""



    if 100 < a or a == 1 or a == 0:
        return False
    i = 2
    while i * i <= a:
        if a % i == 0:
            if is_prime(i):
                j = i + 1
                while j * j <= a:
                    if a % j == 0:
                        if is_prime(j):
                            return True
                        j += 1
                    j += 1
        i += 1
    return False


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


print(is_multiply_prime(10))
print(is_multiply_prime(15))
print(is_multiply_prime(30))
print(is_multiply_prime(20))
print(is_multiply_prime(12))
print(is_multiply_prime(35))
