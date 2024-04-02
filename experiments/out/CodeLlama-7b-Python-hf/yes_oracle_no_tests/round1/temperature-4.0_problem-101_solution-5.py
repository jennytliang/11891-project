def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    words = s.replace(", ", " ").split()
    return words


def no_punctuation(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    no_punctuation("Hi, my name is John") == "Hi my name is John"
    no_punctuation("Hello, World!") == "Hello World"
    no_punctuation(":.,;')(-") == ""
    """
    return s.replace(",", "").replace(".", "").replace(";", "").replace("'", "").replace("(", "").replace(")", "")


def get_first_word(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return the first word.
    
    For example:
    get_first_word("Hi my name is John") == "Hi"
    get_first_word("Hello world") == "Hello"
    get_first_word("One, two, three, four, five, six") == "One"
    """
    return s.split()[0]


def get_first_two_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return the first two words.
    
    For example:
    get_first_two_words("Hi my name is John") == "Hi my"
    get_first_two_words("Hello world") == "Hello world"
    get_first_two_words("One, two, three, four, five, six") == "One, two"
    """
    return s.split()[:2]


def get_last_word(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return the last word.
    
    For example:
    get_