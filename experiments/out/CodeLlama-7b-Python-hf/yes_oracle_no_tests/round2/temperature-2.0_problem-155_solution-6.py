def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    for i in num:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# print(even_odd_count(-12))
# print(even_odd_count(123))


def reverse_string(string):
    """Given a string. Reverse the string without using any built-in functions.

	Example:
	    reverse_string('asdf') ==> 'fdsa'
	"""
    new_string = ''
    for i in string:
        new_string = i + new_string
    return new_string


# print(reverse_string('asdf'))


def is_palindrome(string):
    """Given a string. Check if it is palindrome or not.

	Example:
	    is_palindrome('abcdcba') ==> True
	"""
    rev_string = reverse_string(string)
    if rev_string == string:
        return True
    else:
        return False


# print(is_palindrome('abcdcba'))


def is_prime(num):
    """Given a number. Check if it is prime or not.

	Example:
	    is_prime(10) ==> False
	"""
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# print(is_prime(10))


def is_perfect_square(num):
    """Given a number. Check if it is a perfect square or not.

	Example:
	    is_perfect_square(14) ==> False
	"""
    return (int(num ** 0.5) ** 2) == num


# print(is_perfect_square(14))


def is_capital(string):
    """Given a string. Check if it is in all capital letters or not.

	Example:
	   