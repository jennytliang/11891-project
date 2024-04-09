def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	"""
    return s.split()


def first_word(string):
    """
    You will be given a string of words separated by commas, semi-colons or spaces.
    Your task is to return the first word in the string.
    
    For example:
    first_word("Hello world") == "Hello"
    first_word("Hello world, this is my world") == "Hello"
    first_word("One, two, three, four, five, six") == "One"
    first_word("One two three four five six") == "One"
    
	Include these tokens in the code: words
	"""
    return string.split()[0]


def last_word(string):
    """
    You will be given a string of words separated by commas, semi-colons or spaces.
    Your task is to return the last word in the string.
    
    For example:
    last_word("Hello world") == "world"
    last_word("Hello world, this is my world") == "world"
    last_word("One, two, three, four, five, six") == "six"
    last_word("One two three four five six") == "six"
    
	Include these tokens in the code: words
	"""
    return string.split()[-1]


def middle_word(string):
    """
    You will be given a string of words separated by commas, semi-colons or spaces.
    Your task is to return the middle word in the string.
    
    For example:
    middle_word("Hello world") == "world"
    middle_word("Hello world, this is my world") == "world"
    middle_word("One, two, three, four, five, six") == "three"
    middle_word("One two three four five six") == "three"
    
	Include these tokens in the code: words
	"""
    return string.split()[1]


def upcase_words(string):
    """
    You will be given a string of words separated by commas, semi-colons or spaces.
   