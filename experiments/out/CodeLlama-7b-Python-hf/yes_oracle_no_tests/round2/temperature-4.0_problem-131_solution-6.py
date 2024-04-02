def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # YOUR CODE HERE
    prod = 1
    for i in str(n):
        if int(i) % 2 == 1:
            prod *= int(i)
    return prod


# print(digits(1))
# print(digits(4))
# print(digits(235))
# print(digits(12345))

def sum_digits(n):
    """Given a non-negative integer n, return the sum of its digits.
    For example:
    sum_digits(123) == 6
    HINT: Modular division is the key here.
    """
    # YOUR CODE HERE
    return sum(int(i) for i in str(n))


# print(sum_digits(123))
# print(sum_digits(12345))
# print(sum_digits(123456789))
# print(sum_digits(1234567890))

def is_prime(n):
    """Return True if n is a prime number, otherwise return False.
    For example:
    is_prime(123) == True
    is_prime(1234) == False
    is_prime(1234567890) == True
    """
    # YOUR CODE HERE
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# print(is_prime(123))
# print(is_prime(1234))
# print(is_prime(1234567890))

def is_palindrome(s):
    """Return True if s is palindrome, otherwise return False.
    For example:
    is_palindrome('radar') == True
    is_palindrome('radars') == False
    is_palindrome('radarsa') == True
    """
