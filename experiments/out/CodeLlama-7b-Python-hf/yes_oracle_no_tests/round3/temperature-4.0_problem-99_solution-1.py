def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    
	Include these tokens in the code: def round ing ( val ):
	'''
    # your code here


def check_palindrome(string):
    '''
    Create a function that takes a string and returns True if it is
    a palindrome.

    Examples
    >>> check_palindrome("tacocat")
    True
    >>> check_palindrome("hello")
    False

    Note:
    You can use the function str.lower() to convert strings to lowercase.
    '''
    # your code here


def find_longest_word(string):
    '''
    Create a function that takes a string and returns the longest
    word in the string.

    Examples
    >>> find_longest_word("The quick brown fox jumped over the lazy dog")
    'jumped'
    >>> find_longest_word("May I borrow this book?")
    'book'

    Note:
    You can use the function str.split() to split a string into a
    list of words.
    '''
    # your code here


def find_longest_word_recursively(string):
    '''
    Create a function that takes a string and returns the longest
    word in the string.

    Examples
    >>> find_longest_word_recursively("The quick brown fox jumped over the lazy dog")
    'jumped'
    >>> find_longest_word_recursively("May I borrow this book?")
    'book'

    Note:
    You should use recursion to solve this problem.
    '''
    # your code here


def is_prime(num):
    '''
    Create a function that takes a number and returns True if it is
    a prime number.

    Examples
    >>> is_prime(13)
    True
    >>> is_prime(12)
    False

    Note:
    You can use the function range to iterate over a sequence of numbers.
    '''
    # your code here


def is_reverse(num1, num2):
    '''
    Create a function that takes two numbers and returns True if
    they are the reverse of each