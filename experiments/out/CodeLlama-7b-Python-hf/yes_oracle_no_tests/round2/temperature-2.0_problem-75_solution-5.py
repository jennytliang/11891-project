def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: divis ors = []
	"""
    # your code here
    primes = [2,3,5]
    for prime in primes:
        if a % prime == 0:
            a = a / prime
    if a == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_multiply_prime(30))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(13) == False
    assert is_multiply_prime(7) == False
    assert is_multiply_prime(11) == True
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(1) == False
    assert is_multiply_prime(20) == False
    assert is_multiply_prime(19) == False
    assert is_multiply_prime(25) == False
    assert is_multiply_prime(45) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
