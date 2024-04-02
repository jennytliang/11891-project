def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Do not include these tokens in the code: words = s . replace (", ",
	"""
	""")
	return words.split ()

    """
    :param s: string
    :return: list of strings
    """
    return s.replace(",", " ").replace(", ", " ").replace("  ", " ").split(" ")


def convert_string_to_int(s):
    """
    You will be given a string of numbers separated by commas or spaces. Your task is to
    split the string into numbers and return an array of the numbers.
    
    For example:
    convert_string_to_int("1, 2, 3, 4, 5, 6") == [1, 2, 3, 4, 5, 6]
    convert_string_to_int("1,2,3,4,5,6") == [1,2,3,4,5,6]
    
	Do not include these tokens in the code: numbers = s . replace (",", " ")
    return numbers.split ()
    
    """
    return [int(n) for n in s.replace(",", " ").replace(", ", " ").replace("  ", " ").split(" ")]


def count_substring(string, sub_string):
    """
    You will be given a string and a substring. You need to find how many times the
    substring occurs in the given string.
    
    For example:
    count_substring("holaHolajola", "hola") == 2
    count_substring("bobobobobob", "bob") == 4
    
    """
    return string.count(sub_string)


def check_url(url):
    """
    You will be given a string that may or may not be a valid URL. You need to write a
    regular expression that matches URLs. There are several types of URLs that you need
    to match, including:
    
    http://www.example.com
    http://example.com
    www.example.com
    example.com
    
    """
    import re
    return bool(re.match("^((https?:\/\/|www\.)?