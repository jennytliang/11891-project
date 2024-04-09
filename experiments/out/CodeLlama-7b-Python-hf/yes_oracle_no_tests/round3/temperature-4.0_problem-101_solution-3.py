def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.replace(", "," ").split()


def count_substring(string, sub_string):
    """
    Count the frequency of sub_string in string.
    
    For example:
    count_substring("ABCDCDC", "CDC") == 2
    count_substring("ABCDCDC", "CCD") == 0
    count_substring("ABCDCDC", "ABC") == 1
    
    If sub_string is not found in string, return 0.
    """
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


def camel_case(s):
    """
    You will be given a word consisting of letters. Your task is to find out if the given word
    is a camel case string. In a camel case string, letters are case sensitive and they should be
    divided by an underscore if they are not capital.
    
    For example:
    camel_case("camelCase") == True
    camel_case("camel_Case") == True
    camel_case("camel2Case") == False
    camel_case("camelCase2") == False
    
	If the given word is a camel case string, return 1. Otherwise, return 0.
    """
    for i in range(1, len(s)):
        if s[i].isupper() and s[i - 1].islower():
            return 0
    return 1


def remove_duplicates(s):
    """
    Given a string, you need to remove all duplicates.
    
    For example:
    remove_duplicates("aabbbbc") == "abc"
    remove_duplicates("aabbdbc") == "adc"
    
    If there is no duplicate, return the original string.
    """
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s
    if s[0] != s[1]:
        return s