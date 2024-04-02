def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	"""
    return s.replace(',', ' ').split()


# TESTS
assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
assert words_string("Hello") == ["Hello"]
assert words_string("") == []
