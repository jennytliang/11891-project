def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Do not include these tokens in the code: pass def is _ equal
	"""
    # YOUR CODE HERE
    if n % 2 == 1:
        return False
    else:
        even_num = n / 2
        even_num_list = list(range(even_num, 0, -2))
        for i in even_num_list:
            for j in even_num_list:
                for k in even_num_list:
                    for l in even_num_list:
                        if i + j + k + l == n:
                            return True
        return False



def sum_of_divisors(n):
    """Return the sum of all positive integer divisors of n
    Example
    sum_of_divisors(6) == 12
    sum_of_divisors(12) == 31
    
	Do not include these tokens in the code: pass def sum_of_divisors
	"""
    # YOUR CODE HERE
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)



def is_prime(n):
    """Evaluate whether the given number n is prime
    Example
    is_prime(2) == True
    is_prime(8) == False
    
	Do not include these tokens in the code: pass def is_prime
	"""
    # YOUR CODE HERE
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True



def is_prime_with_divisors(n):
    """Evaluate whether the given number n is prime and has exactly 4 positive integer divisors
    Example
    is_prime_with_divisors(7) == True
    is_prime_with_divisors(12) == False
    
	Do not include these tokens in the code: pass def is_prime_with_divisors
	""