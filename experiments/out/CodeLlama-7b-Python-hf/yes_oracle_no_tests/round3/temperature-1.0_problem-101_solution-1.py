def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Do not include these tokens in the code: return s . replace (", ", "
	"""
    return s.replace(",", " ").split()


print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))


# 2. is_even
def is_even(n):
    """
    You will be given a number. You should return True if the number is even, and False
    if the number is odd.
    
    For example:
    is_even(2) == True
    is_even(5) == False
    """
    return n % 2 == 0


print(is_even(2))
print(is_even(5))


# 3. is_multiple
def is_multiple(n, m):
    """
    You will be given two numbers. You should return True if the first number is a
    multiple of the second number, and False if it is not.
    
    For example:
    is_multiple(6, 2) == True
    is_multiple(5, 2) == False
    """
    return n % m == 0


print(is_multiple(6, 2))
print(is_multiple(5, 2))


# 4. is_prime
def is_prime(n):
    """
    You will be given a number n. You should determine if it is a prime number or not.
    A prime number is a natural number greater than 1 that has no positive divisors
    other than 1 and itself.
    
    For example:
    is_prime(5) == True
    is_prime(15) == False
    """
    return all(n % i for i in range(2, n))


print(is_prime(5))
print(is_prime(15))


# 5. is_pandigital
def is_pandigital(n):
    """
    You will be given a number n. A pandigital number is a number where all the digits
    from 1 to n are present when n is written in base 10.
    
    For example