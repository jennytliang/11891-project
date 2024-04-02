def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    
	Include these tokens in the code: words
	Do not include these tokens in the code: app les
	"""
    #code
    return n - int(s.split()[0]) - int(s.split()[2])

def is_palindrome(string):
    """
    A palindrome is a string that reads the same forward and backward, 
    eg: madam or 12321.
    Given a string check if it is palindrome.
    for examble:
    is_palindrome("madam") -> True
    is_palindrome("Hello") -> False
    is_palindrome("1000") -> True
    is_palindrome("12345") -> False
    
	Include these tokens in the code: palindrome
	Do not include these tokens in the code: palindrome
    """
    #code
    return string == string[::-1]

def string_mixer(string1,string2):
    """
    In this task, you will be given a string of lowercase english letters and you will be given 
    another string of lowercase english letters.
    Return a string that contains all of the characters from the first string and all of the 
    characters from the second string.
    for examble:
    string_mixer("abc", "def") -> "adbecf"
    string_mixer("abcd", "def") -> "adbefcd"
    string_mixer("abc", "defg") -> "adbecf"
    string_mixer("abc", "") -> "abc"
    
	Include these tokens in the code: string1 string2
	Do not include these tokens in the code:
    """
    #code
    return string1 + string2

def count_substring(string, sub_string):
    """
    Given a string and a substring, count the number of times the substring occurs in the string.
    for examble:
    count_substring("ABCDCDC", "CDC") -> 2
    count_substring("ABCDCDC", "CDD") -> 0
    count_substring("ABCDCDC", "ABCD") -> 1
    count_substring("", "ABCD