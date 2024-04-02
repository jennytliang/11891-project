def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: 0 0
	"""


    if  a < 30:
        return False
    
    for i in range(3, 10):
        if is_prime(i) and is_prime(a//i) and is_prime(a//(a//i)):
            return True
    
    return False


def is_prime(a):
    """
    Write a function that returns true if the given number is prime and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_prime(3) == True
    is_prime(30) == False
    """

    for i in range(2, a):
        if a % i == 0:
            return False
    return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_multiply_prime(30) == True, "30 = 2 * 3 * 5"
    assert is_multiply_prime(225) == True, "225 = 5 * 5 * 5"
    assert is_multiply_prime(9) == False, "9 is single prime number"
    assert is_multiply_prime(12) == False, "12 is not multiply prime"
    assert is_multiply_prime(15) == False, "15 is not multiply prime"
    assert is_multiply_prime(33) == False, "33 is not multiply prime"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
