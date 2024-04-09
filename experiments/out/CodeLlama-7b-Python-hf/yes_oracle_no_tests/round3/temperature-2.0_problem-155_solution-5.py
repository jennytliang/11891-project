def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    for i in str(num):
        i = int(i)
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# print(even_odd_count(-12))
# print(even_odd_count(123))
# print(even_odd_count(123456789))


def is_palindrome(text):
    """Given a string, return a boolean indicating whether or not it is a palindrome.

    A palindrome is defined as "a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run."

    Example:
        is_palindrome("madam") == True
        is_palindrome("nurses run") == True
        is_palindrome("Hello") == False
    """
    return text == text[::-1]


# print(is_palindrome("madam"))
# print(is_palindrome("nurses run"))
# print(is_palindrome("Hello"))


def is_prime(num):
    """Given an integer, return a boolean indicating whether or not it is prime.

    A prime number is defined as a number that can only be evenly divided by 1 and itself.

    Example:
    is_prime(1) == False
    is_prime(2) == True
    is_prime(11) == True
    """
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# print(is_prime(1))
# print(is_prime(2))
# print(is_prime(11))
# print(is_prime(10))


def is_prime_v2(num):
    """Given an integer, return a boolean indicating whether or not it is prime.

    A prime number is