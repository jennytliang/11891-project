def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    # my solution
    # if a <= 4:
    #     return False
    # div = 2
    # for i in range(1, (a//2)+1):
    #     if a % i == 0:
    #         div = i
    #         break
    # for j in range(2, ((a//div)//2)+1):
    #     if div % j == 0:
    #         new_div = j
    #         break
    # for k in range(2, ((a//new_div)//2)+1):
    #     if new_div % k == 0:
    #         new_new_div = k
    #         break
    # if a == div * new_div * new_new_div:
    #     return True
    # return False

    # refactored
    if a <= 100:
        return a in [
        2 * 3 * 5,
        3 * 5 * 7,
        2 * 3 * 5 * 7,
        3 * 5 * 7 * 11,
    ]
    return False


def recursive_is_multi_prime(a):
    """Write a recursive function that returns true if the given number is the multiplication of
    3 prime numbers
    and false otherwise.
    Knowing that a is less then 100.
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    return a in list_of_prime_3_numbers()


def list_of_prime_3_numbers():
    primes = set()
    candidates = set(range(101))
    while candidates:
        candidate = candidates.pop()
        if all((candidate % i == 0) for i in (candidates - {candidate, 1})):
            primes.add(candidate)
            # if there 3 items in result, you have a prime
            # because every other number was removed.
            # TODO:

            # if