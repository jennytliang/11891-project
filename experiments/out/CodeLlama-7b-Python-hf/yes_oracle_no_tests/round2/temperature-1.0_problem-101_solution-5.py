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


def is_palindrome(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to create a function that will return True if the string is a palindrome.
    
    For example:
    is_palindrome("tacocat") == True
    is_palindrome("cat") == True
    is_palindrome("I love spaghetti!") == False
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.replace(", ", " ").replace("!", "").replace(".", "").replace(",", "").replace("?", "").replace(";", "").lower() == s.replace(", ", " ").replace("!", "").replace(".", "").replace(",", "").replace("?", "").replace(";", "").lower()[::-1]


def is_reverse_palindrome(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to create a function that will return True if the string is a reverse palindrome.
    A reverse palindrome is a string that is a palindrome reading backwards.
    
    For example:
    is_reverse_palindrome("tacocat") == True
    is_reverse_palindrome("cat") == True
    is_reverse_palindrome("I love spaghetti!") == False
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.replace(", ", " ").replace("!", "").replace(".", "").replace(",", "").replace("?", "").replace(";", "").lower() == s.replace(", ", " ").replace("!", "").replace(".", "").replace(",", "").replace("?", "").replace(";", "").lower()[::-1]


def is_number(s):
    """
    You will be given a string of words separated by commas or spaces.