def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	Do not include these tokens in the code: wo
	"""
    return s.replace(" ","").split(",")


def is_even(n):
    """
    You will be given a number n and you will need to return True if n is even, and False otherwise.
    
	For example:
	is_even(2) == True
	is_even(5) == False
	is_even(0) == True
	"""
    return n % 2 == 0


def is_multiple(n, m):
    """
    You will be given two numbers n and m, and you will need to return True if n is a multiple of m, and False otherwise.
    
    For example:
    is_multiple(6, 2) == True
    is_multiple(5, 2) == False
    is_multiple(6, 3) == False
    """
    return n % m == 0


def is_prime(n):
    """
    You will be given a number n and you will need to return True if it is a prime number, and False otherwise.
    
	For example:
	is_prime(2) == True
	is_prime(15) == False
	is_prime(51) == True
	is_prime(47) == True
	"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_palindrome(s):
    """
    You will be given a string s, and you will need to return True if it is a palindrome, and False otherwise.
    
    For example:
    is_palindrome("abba") == True
    is_palindrome("abcba") == True
    is_palindrome("abbc") == False
    is_palindrome("abcd") == False
    """
    return s == s[::-1]


def is_vowel(c):
    """
    You will be given a single English letter. You need to return True if it is a vowel, and False otherwise.
    
    For example:
    is_vowel("a