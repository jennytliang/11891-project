def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    for i in range(1, a + 1):
        if is_prime(i):
            for j in range(1, a + 1):
                if is_prime(j):
                    for k in range(1, a + 1):
                        if is_prime(k):
                            if i * j * k == a:
                                return True
    return False


def test_is_multiply_prime():
    assert is_multiply_prime(30) == True

if __name__ == '__main__':
    test_is_multiply_prime()
