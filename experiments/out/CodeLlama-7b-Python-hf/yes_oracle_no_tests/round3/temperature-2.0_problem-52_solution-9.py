def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


    return all(x < t for x i l)


def unique(l: list):
    """Returns True if all the elements in the list are unique
    >>> unique([1, 2, 3, 4, 5])
    True
    >>> unique([1, 2, 3, 4, 1, 5])
    False
    
    Do not include these tokens in the code: if __ name __ == " __ main __
    """


    return len(set(l)) == len(l)


def sum_up_to(n: int):
    """Returns the sum of the numbers between 0 and n.
    >>> sum_up_to(5)
    10
    >>> sum_up_to(2)
    3
    >>> sum_up_to(100)
    5050
    
    Do not include these tokens in the code: if __ name __ == " __ main __
    """


    return (n * (n + 1)) / 2


def is_prime(n: int):
    """Returns True if the number is prime, False otherwise.
    >>> is_prime(5)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    
    Do not include these tokens in the code: if __ name __ == " __ main __
    """


    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def sum_primes(n: int):
    """Returns the sum of all prime numbers between 0 and n.
    >>> sum_primes(5)
    5
    >>> sum_primes(10)
    17
    >>> sum_primes(100)
    1060
    
    Do not include these tokens in the code: if __ name __ == " __ main __
    """


    return sum(i