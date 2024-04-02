def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    #
    # WRITE YOUR CODE HERE
    #
    if a <= 100:
        if a > 1:
            for i in range(2, a):
                if a % i == 0:
                    count = 0
                    for j in range(2, i):
                        if i % j == 0:
                            count += 1
                    if count == 0:
                        return True
            return False
        else:
            return False
    else:
        return False


def is_multiply_prime_2(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    #
    # WRITE YOUR CODE HERE
    #
    if a <= 100:
        if a > 1:
            for i in range(2, a):
                count = 0
                for j in range(2, i):
                    if i % j == 0:
                        count += 1
                if count == 0:
                    for k in range(2, i):
                        count_k = 0
                        for l in range(2, k):
                            if k % l == 0:
                                count_k += 1
                        if count_k == 0:
                            for m in range(2, k):
                                count_m = 0
                                for n in range(2, m):
                                    if m % n == 0:
                                        count_m += 1
                                if count_m == 0:
                                    if i * k * m == a:
                                        return True
            return False
        else:
            return False
    else:
        return False


print(is