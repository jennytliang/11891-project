def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: <=  1
	Do not include these tokens in the code: < 0 0
	"""

    if a  <= 1:
        return False
    
    if a == 2 or a == 3 or a == 5:
        return True
    
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        return False
    
    i = 1
    while i <= a ** 0.5:
        if a % i == 0:
            if is_prime(i):
                j = i + 1
                while j <= a ** 0.5:
                    if a % j == 0:
                        if is_prime(j):
                            k = j + 1
                            while k <= a ** 0.5:
                                if a % k == 0:
                                    if is_prime(k):
                                        return True
                                k += 1
                        j += 1
        i += 1
    return False

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True