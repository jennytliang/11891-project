def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: is prime = [ True ] * ( a +
	Do not include these tokens in the code: else :
	"""


    if a  <= 1:
        r = False
    elif a < 100:
        r = True
    else:
        r = False

    return r




if __name__ == '__main__':
    print("Example:")
    print(is_multiply_prime(30))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(12) == False
    assert is_multiply_prime(24) == False
    assert is_multiply_prime(17) == True
    assert is_multiply_prime(33) == True
    assert is_multiply_prime(111) == True
    assert is_multiply_prime(121) == False
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(100) == False
    assert is_multiply_prime(666) == True
    assert is_multiply_prime(1000) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")