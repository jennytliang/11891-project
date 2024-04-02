def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r anger
	"""


    foobar = []
    for i in range(1, n):
        if n % i == 0:
            foobar.append(i)
    return max(foobar)

print(largest_divisor(15))
print(largest_divisor(25))
print(largest_divisor(12))
print(largest_divisor(17))
print(largest_divisor(27))
print(largest_divisor(5))
print(largest_divisor(24))
print(largest_divisor(10))
print(largest_divisor(1))
print(largest_divisor(6))
print(largest_divisor(14))
print(largest_divisor(18))
print(largest_divisor(19))
print(largest_divisor(23))
print(largest_divisor(26))
print(largest_divisor(31))
print(largest_divisor(35))
print(largest_divisor(40))
print(largest_divisor(45))
print(largest_divisor(47))
print(largest_divisor(49))
print(largest_divisor(51))
print(largest_divisor(53))
print(largest_divisor(55))
print(largest_divisor(57))
print(largest_divisor(59))
print(largest_divisor(61))
print(largest_divisor(65))
print(largest_divisor(70))
print(largest_divisor(75))
print(largest_divisor(79))
print(largest_divisor(85))
print(largest_divisor(89))
print(largest_divisor(90))
print(largest_divisor(95))
print(largest_