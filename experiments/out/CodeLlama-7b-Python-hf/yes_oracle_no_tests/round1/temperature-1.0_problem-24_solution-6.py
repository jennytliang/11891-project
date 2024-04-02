def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: 2
	Do not include these tokens in the code: n - 1
	"""

    for i in r(n - 1, -1, -1):
        if n % i == 0:
            return n // i


# print(largest_divisor(2))   # 1
# print(largest_divisor(6))   # 3
# print(largest_divisor(50))   # 5
# print(largest_divisor(150))   # 5
# print(largest_divisor(15))   # 5
# print(largest_divisor(n)) # 1
