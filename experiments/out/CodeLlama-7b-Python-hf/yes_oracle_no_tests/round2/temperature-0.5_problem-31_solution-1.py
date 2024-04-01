def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    
	Include these tokens in the code: n _ sqrt = 1
	"""


    if n  <= 1:
      return False
    sqrt = 1
    
    if n > 1:
      for i in range(2, int(sqrt)):
        if n % i == 0:
          return False
        sqrt = i + 1
      return True

def prime_factors(n):
    """Return a list of the prime factors of a given number.
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(7)
    [7]
    >>> prime_factors(105)
    [3, 5, 5]
    
    Include these tokens in the code: n factors = []
    """

    factors = []
    while n % 2 == 0:
      factors.append(2)
      n = n / 2

    for i in range(3, int(n**0.5) + 1, 2):
      while n % i == 0:
        factors.append(i)
        n = n / i

    if n > 2:
      factors.append(n)
      
    return factors


def is_prime_power(n):
    """Return True if n is a prime power, and False otherwise.
    >>> is_prime_power(10)
    True
    >>> is_prime_power(15)
    False
    >>> is_prime_power(9)
    True
    >>> is_prime_power(12)
    False
    >>> is_prime_power(17)
    True
    >>> is_prime_power(24)
    False
    >>> is_prime_power(25)
    True
    >>> is_prime_power(32)
    True
    >>> is_prime_power(2)
    True
    >>> is_prime_power(1)
    True
    >>> is_prime_power(0)
    False
    
    Include these tokens in the code: n factor = 