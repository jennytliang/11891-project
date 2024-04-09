def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.replace(", ", " ").split(" ")


def is_palindrome(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to check if every word is a palindrome and return an array with the result.
    
    For example:
    is_palindrome("malayalam, madam") == [True, True]
    is_palindrome("Lisa Bonet ate no basil") == [False, True, False, True, False]
    is_palindrome("One, two, three, four, five, six") == [False, False, False, False, False, False]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return [word == word[::-1] for word in s.replace(", ", " ").split(" ")]


def is_palindrome2(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to check if every word is a palindrome and return an array with the result.
    
    For example:
    is_palindrome("malayalam, madam") == [True, True]
    is_palindrome("Lisa Bonet ate no basil") == [False, True, False, True, False]
    is_palindrome("One, two, three, four, five, six") == [False, False, False, False, False, False]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return [word == word[::-1] for word in s.split()]


def is_palindrome3(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to check if every word is a palindrome and return an array with the result.
    
    For example:
    is_palindrome("malayalam, madam") == [True, True]
    is_palind