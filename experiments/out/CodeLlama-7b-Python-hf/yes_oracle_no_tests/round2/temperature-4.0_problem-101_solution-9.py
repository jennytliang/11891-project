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


def reverse_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to reverse the string and return it as an array of the words in reverse order.

    For example:
    reverse_words("Hi, my name is John") == ["John", "is", "name", "my", "Hi"]
    reverse_words("One, two, three, four, five, six") == ["six", "five", "four", "three", "two", "One"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    words = s.replace(", ", " ")
    return words.split()[::-1]


def reverse_if_odd(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to check if the number of words in the string is odd. If the number of words is
    odd, then reverse the whole string (not the words), otherwise don't change the
    string.
    
    For example:
    reverse_if_odd("One, two, three") == "three, two, One"
    reverse_if_odd("One, two, three, four") == "One, two, three, four"
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    words = s.replace(", ", " ")
    if len(words.split()) % 2 != 0:
        return words[::-1]
    return s


def make_upper(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to capitalize all letters of the given string.
    
    For example:
    make_upper("hello, world") == "HELLO, WORLD"
    make_upper("a message, to follow") == "A MESSAGE, TO FOLLOW"
    
	Include these tokens in the code: words =