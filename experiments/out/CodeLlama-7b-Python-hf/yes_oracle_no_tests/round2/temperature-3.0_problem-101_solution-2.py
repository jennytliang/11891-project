def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    words = s.replace(", ", " ")
    return words.split()

def is_palindrome(s):
    """
    A palindrome is a string that reads the same backwards and forwards.
    For example, "racecar" and "madam" are palindromes.
    Return True if s is a palindrome, and False otherwise.
    
    You may assume that all characters present in s are alphabetic.
    
    words_string("racecar") == True
    words_string("race car") == False
    """
    return s == s[::-1]

def is_reverse_palindrome(s):
    """
    A reverse palindrome is a string that reads the same backwards and forwards, but in reverse order.
    For example, "racecar" and "maracar" are reverse palindromes.
    Return True if s is a reverse palindrome, and False otherwise.
    
    You may assume that all characters present in s are alphabetic.
    
    words_string("racecar") == True
    words_string("race car") == False
    """
    return s == s[::-1]

def has_palindrome(s):
    """
    Return True if s contains a palindrome, and False otherwise.
    
    You may assume that all characters present in s are alphabetic.
    
    words_string("racecar") == True
    words_string("race car") == True
    """
    for i in range(len(s)):
        for j in range(len(s) - i):
            if is_palindrome(s[i:i+j+1]):
                return True
    return False

def has_reverse_palindrome(s):
    """
    Return True if s contains a reverse palindrome, and False otherwise.
    
    You may assume that all characters present in s are alphabetic.
    
    words_string("racecar") == True
    words_string("race car") == True
    """
    for i in range(len(s)):
        for