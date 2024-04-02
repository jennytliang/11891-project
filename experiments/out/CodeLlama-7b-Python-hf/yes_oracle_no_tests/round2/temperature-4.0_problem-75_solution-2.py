def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: # 1 is not a prime
	"""
    # Find the first prime number
    prime = 1
    while True:
        is_prime = True
        for i in range(2, prime):
            if prime % i == 0:
                is_prime = False
                break
        if is_prime:
            break
        prime += 1
    # Find the second prime number
    while True:
        is_prime = True
        for i in range(2, prime):
            if prime % i == 0:
                is_prime = False
                break
        if is_prime:
            break
        prime += 1
    # Find the third prime number
    while True:
        is_prime = True
        for i in range(2, prime):
            if prime % i == 0:
                is_prime = False
                break
        if is_prime:
            break
        prime += 1
    # Check if the given number is the multiplication of 3 prime numbers
    return a == prime * prime * prime


if __name__ == '__main__':
    print("Example:")
    print(is_multiply_prime(30))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(12) == False
    assert is_multiply_prime(31) == False
    assert is_multiply_prime(45) == True
    assert is_multiply_prime(63) == False
    assert is_multiply_prime(87) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
