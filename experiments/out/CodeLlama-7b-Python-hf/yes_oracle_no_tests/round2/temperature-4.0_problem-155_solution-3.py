def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: , odd
	"""

    # pass
    count_even = 0
    count_odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd


# TEST
# print(even_odd_count(-12))  # (1, 1)
# print(even_odd_count(123))  # (1, 2)

# =====================================================================================

def is_prime(num):
    """Given a number, return True if prime or False if not.

    Example:
        is_prime(11) ==> True
        is_prime(12) ==> False
    
    Note: You can use the isPrime function from the previous exercise.
	"""

    # pass
    if num < 0:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


# TEST
# print(is_prime(11))  # True
# print(is_prime(12))  # False

# =====================================================================================

def is_prime_v2(num):
    """Given a number, return True if prime or False if not.

    Example:
        is_prime_v2(11) ==> True
        is_prime_v2(12) ==> False
    
    Note: You can use the isPrime function from the previous exercise.
	"""

    # pass
    if num < 0:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0: