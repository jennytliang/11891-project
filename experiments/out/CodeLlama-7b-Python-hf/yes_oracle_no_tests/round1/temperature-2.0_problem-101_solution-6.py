def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.replace(", ", " ").split()


def extract_numbers(s):
    """
    You will be given a string of words.
    Your task is to extract all numbers from the string
    and return them as a list of integers.
    
    For example:
    extract_numbers("Hi, my name is John 123") == [123]
    extract_numbers("Some 1 12 simple words 123 1 23 456") == [1, 12, 123, 23, 456]
    extract_numbers("") == []
    """
    return [int(x) for x in s.split() if x.isdigit()]


def reverse_string(s):
    """
    Reverse a given string.
    
    For example:
    reverse_string("val") == "lav"
    reverse_string("hello") == "olleh"
    """
    return s[::-1]


def is_palindrome(s):
    """
    Determine whether a given string is a palindrome.
    A palindrome is defined as a string that is written
    in the same direction and reads the same forwards and backwards.
    
    For example:
    is_palindrome("val") == False
    is_palindrome("ola") == True
    is_palindrome("bob") == True
    is_palindrome("anna") == True
    is_palindrome("12345654321") == True
    is_palindrome("1234567") == False
    is_palindrome("racecar") == True
    is_palindrome("aabb") == True
    is_palindrome("aba") == True
    is_palindrome("") == True
    is_palindrome("x") == True
    """
    return s == s[::-1]


def is_unique(s):
    """
    Determine whether a given string has all unique characters.
    
   