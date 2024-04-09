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


def unique_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to find all the unique words.
    
    For example:
    unique_words("Hi, my name is John, my name is Mike") == ["Hi", "my", "name", "John", "Mike"]
    unique_words("One, two, three, four, five, six, one, two, three") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return list(set(s.replace(", ", " ").split(" ")))


def remove_empty_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to remove all the empty words and return an array of the non-empty words.
    
    For example:
    remove_empty_words("Hi, my name is John, my name is Mike, , , ,") == ["Hi", "my", "name", "John", "Mike"]
    remove_empty_words("One, two, three, four, five, six, ") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.replace(", ", " ").split(" ")


def uppercase_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to change all the words to their upper case version and return an array of the changed words.
    
    For example:
    uppercase_words("Hi, my name is John") == ["HI", "MY", "NAME", "IS", "JOHN"]
    uppercase_words("One, two, three, four, five, six") == ["ONE", "TWO", "THREE", "FOUR", "FIVE",