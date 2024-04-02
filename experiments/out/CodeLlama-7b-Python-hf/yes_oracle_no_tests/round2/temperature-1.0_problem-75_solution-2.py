def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: # my solution #
	"""
    primes, result = [], []

    for n in range(2, a + 1):

        prime = 1  # 1 is not prime
        for factor in range(2, n):
            if n % factor == 0:
                prime += 1
                break

        if prime:
            primes.append(n)

    return len(primes) == 3


def test_is_multiply_prime():
    assert is_multiply_prime(6) is True
    assert is_multiply_prime(26) is False
    assert is_multiply_prime(60) is True

    print 'Passed'


if __name__ == '__main__':
    test_is_multiply_prime()
