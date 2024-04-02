def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    # Your code here
    return s.replace(", ", " ").split()


def first_word(string):
    """
    Given a string of words separated by spaces, return the first word in the string.
    
    For example:
    first_word("Hi, my name is John") == "Hi"
    first_word("One, two, three, four, five, six") == "One"
    """
    # Your code here
    return string.split()[0]


def last_word(string):
    """
    Given a string of words separated by spaces, return the last word in the string.
    
    For example:
    last_word("Hi, my name is John") == "John"
    last_word("One, two, three, four, five, six") == "six"
    """
    # Your code here
    return string.split()[-1]


def middle_words(string):
    """
    Given a string of words separated by spaces, return the middle word(s) in the string.
    
    For strings with an odd number of words, return the middle word and the one after it;
    for an even number of words, return the middle words.
    
    For example:
    middle_words("Hi, my name is John") == "my"
    middle_words("One, two, three, four, five, six") == "four"
    middle_words("Lorem ipsum dolor sit amet") == "ipsum dolor"
    """
    # Your code here
    return string.split()[len(string.split()) // 2]


def sort_words(string):
    """
    Given a string of words, return a string of the words sorted
    alphabetically.
    
    For example:
    sort_words("Lorem ipsum dolor sit amet") == "Lorem ipsum amet dolor sit"
    """
    # Your code here
    return " ".join(sorted(string.split()))


def sort_backwards(string):
    """
    Given a string of words, return a string of the words sorted
    backwards, separated by spaces.
    
