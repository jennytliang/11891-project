def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	"""
    return s.replace(',',' ').split()


def no_punctuation(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is to
    split the string into words and return an array of the words.
    
    For example:
    no_punctuation("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    no_punctuation("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	"""
    return s.replace(',',' ').replace('.',' ').replace(';',' ').replace(':',' ').split()


def all_caps(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is to
    split the string into words and return an array of the words.
    
    For example:
    all_caps("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    all_caps("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	"""
    return s.replace(',',' ').replace('.',' ').replace(';',' ').replace(':',' ').split()


def no_vowels(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is to
    split the string into words and return an array of the words.
    
    For example:
    no_vowels("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    no_vowels("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	""