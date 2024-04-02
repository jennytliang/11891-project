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


def unique_chars(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to find all the unique characters in that string.
    
    For example:
    unique_chars("Hello, my name is John") == ["H", "e", "l", "o", "m", "n", "i", "s", "J", "o", "h", "n"]
    unique_chars("One, two, three, four, five, six") == ["O", "n", "e", "t", "w", "h", "r", "f", "s", "i", "v", "x", "u"]
    
    Note: you can assume that the string contains only letters and commas/spaces
    """
    return list(set(s.replace(",", " ").replace(" ", "")))


def first_word(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to return the first word in the string.
    
    For example:
    first_word("Hello, my name is John") == "Hello"
    first_word("One, two, three, four, five, six") == "One"
    
    Note: you can assume that the string contains at least one word
    """
    return s.split(",")[0].split(" ")[0]


def last_word(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to return the last word in the string.
    
    For example:
    last_word("Hello, my name is John") == "John"
    last_word("One, two, three, four, five, six") == "six"
    
    Note: you can assume that the string contains at least one word
    """
    return s.split(",")[-1].split(" ")[-1]


def last_word_reversed(s):
    """
    You will be given a string of