def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.split(", ")


def count_substring(string, sub_string):
    """
    You will be given two strings. The first one will be a big string that will contain the second string. 
    You have to count how many times the second string is contained within the first one. 
    It is guaranteed the second string will be contained in the bigger one.
    
    For example:
    count_substring("ABCDCDC", "CDC") == 2
    count_substring("ABCDCDC", "ABCD") == 1
    count_substring("ABCABC", "ABCD") == 0
    
    You will not be given any strings with more than 10000 characters.
    """
    return string.count(sub_string)


def multi_string_replace(string, d):
    """
    You will be given a string and a dictionary containing the words you will need to replace. 
    You have to replace each word in the string with the word in the dictionary.
    The order of the dictionary words doesn't matter.
    
    For example:
    multi_string_replace("simple string", {"simple": "easy", "string": "word"}) == "easy word"
    multi_string_replace("I like fruit", {"I": "You", "fruit": "orange"}) == "You like orange"
    multi_string_replace("Money heist", {"Money": "M", "heist": "h"}) == "M h i s t"
    
    The string can contain all words in the dictionary or none.
    """
    for k, v in d.items():
        string = string.replace(k, v)
    return string


def extract_domain_name(url):
    """
    You will be given a url of a web page. You have to extract the domain name of the page. 
    For example:
    extract_domain_name("http://google.com") == "google"
    extract_domain_name("http://google.co.jp") == "google"
    extract_domain_name("https://youtube.com") ==