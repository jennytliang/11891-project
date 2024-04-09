def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s
	Do not include these tokens in the code: return
	"""
    words = s.split(", ")
    return words


def split_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    split_words("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    split_words("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s
	Do not include these tokens in the code: return
	"""
    # your code here
    words = s.split(", ")
    return words


def split_words_list_comp(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    split_words("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    split_words("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s
	Do not include these tokens in the code: return
	"""
    # your code here
    words = [word for word in s.split(", ")]
    return words


def split_words_join(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    split_words("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    split_words("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code