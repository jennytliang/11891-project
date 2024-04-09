def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	Do not include these tokens in the code: w
	"""
    return s.replace(',', ' ').split(' ')


def words_string_better(s):
    return s.replace(',', ' ').split(' ')


def words_list(words):
    """
    You will be given a list of words (strings). Your task is to return a list of
    all words that start with the letter "a" or "e" in upper or lower case.
    
    For example:
    words_list(["Hi", "my", "name", "is", "John"]) == ["Hi", "my", "John"]
    words_list(["One", "two", "three", "four", "five", "six"]) == []
    words_list(["aardvark", "abound", "assume", "aware", "awe", "axiom", "be"]) == ["aardvark", "abound", "assume", "aware", "awe", "axiom", "be"]
	"""
    return [word for word in words if word[0] in ('a', 'e')]


def words_list_better(words):
    return [word for word in words if word[0] in ('a', 'e')]


def words_filter(words):
    """
    You will be given a list of words (strings). Your task is to return a list of
    all words that ends with the letter "e".
    
    For example:
    words_filter(["Hi", "my", "name", "is", "John"]) == ["Hi", "name", "John"]
    words_filter(["One", "two", "three", "four", "five", "six"]) == ["one"]
    words_filter(["aardvark", "abound", "assume", "aware", "awe", "axiom", "be"]) == ["aardvark", "assume", "aware", "awe", "axiom"]
    """
    return [word for word in words if word[-1] == 'e']


def words_filter_better(words):
    return [word for word in words if word[-1]