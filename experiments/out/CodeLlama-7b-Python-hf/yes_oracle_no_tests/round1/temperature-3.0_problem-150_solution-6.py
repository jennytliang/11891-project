def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    if is_prime(n):
        return x
    else:
        return y


def is_prime(n):
    """Returns True if n is prime and False otherwise"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# print(x_or_y(7, 34, 12))
# print(x_or_y(15, 8, 5))

# Exercise 2
# Write a function that takes two strings as its inputs, and returns the number of characters that appear in both strings.
# Hint: You can use the .count(str) method to count the number of occurrences of a substring in a string.


def count_common_chars(str1, str2):
    """A simple program which should return the number of characters that appear in both strings

    Examples:
    for count_common_chars("hello", "world") == 1
    for count_common_chars("hello", "hello") == 5
    for count_common_chars("hello", "goodbye") == 0
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    return str1.count(str2)


# print(count_common_chars("hello", "world"))
# print(count_common_chars("hello", "hello"))
# print(count_common_chars("hello", "goodbye"))

# Exercise 3
# Write a function that takes a string as its input, and returns the number of characters that appear in the string at least twice.
# Hint: You can use the .count(str) method to count the number of occurrences of a substring in a string.


def count_chars_at_least_twice(str1):
    """A simple program which should return the number of characters that appear in the string at least twice

    Examples:
    for count_chars_at_least_twice("hello") == 2
    for count_chars_