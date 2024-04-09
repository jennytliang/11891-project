def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: n //
	"""

    for i in range(2, n):
        if n % i == 0:
 
            return i
    return n


if __name__ == "__main__":
    print(largest_divisor(15))
    print(largest_divisor(24))
    print(largest_divisor(50))
    print(largest_divisor(100))
    print(largest_divisor(150))
    print(largest_divisor(1000))
    print(largest_divisor(10000))
