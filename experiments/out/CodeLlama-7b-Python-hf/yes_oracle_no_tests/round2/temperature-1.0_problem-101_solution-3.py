def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
	words = s.lower().split(' ')
	return words

t = 2

def test_function():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"], "Hi"
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"], "One Two"
