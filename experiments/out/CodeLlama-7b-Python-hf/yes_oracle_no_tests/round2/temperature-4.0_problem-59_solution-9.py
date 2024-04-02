def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is
	Do not include these tokens in the code: largest _
	"""
    "*** YOUR CODE HERE ***"
    largest_prime = 0
    while n % 2 == 0:
        largest_prime = 2
        n = n / 2
    for i in range(3, n + 1, 2):
        while n % i == 0:
            largest_prime = i
            n = n / i

    return largest_prime


def sum_of_digits(n: int):
    """Return the sum of the digits of n. Assume n is a positive integer.
    >>> sum_of_digits(10)
    1
    >>> sum_of_digits(4224)
    11
    >>> sum_of_digits(1234)
    10
    
	Include these tokens in the code: is
	Do not include these tokens in the code: sum _
	"""
    "*** YOUR CODE HERE ***"
    sum_of_digits = 0
    while n > 0:
        sum_of_digits += n % 10
        n = n // 10

    return sum_of_digits


def flip_endian(n: int):
    """Return the number with the byte order flipped. Assume n > 0.
    >>> flip_endian(1125899906842624)
    624268992581111
    
	Include these tokens in the code: is
	Do not include these tokens in the code: endian _
	"""
    "*** YOUR CODE HERE ***"
    num = str(n)
    new_num = ""
    for i in range(len(num), 0, -2):
        new_num += num[i - 2] + num[i - 1]

    return int(new_num)


def count_bits(n: int):
    """Return the number of bits that are set to 1 in n.
    >>> count_bits(12)
    3
