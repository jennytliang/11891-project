def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    words = s.replace(", ", " ")
    return words.split()


def first_word(s):
    """
    Given a string of words separated by spaces, return the first word in the string. If the string is empty, return an empty string.
    
    Note:
    - There will always be at least one word in the string.
    - Assume that there are no leading or trailing spaces before or after the list of words.
    - Assume we use the universal newline character \n to separate lines.
    
    Examples:
    first_word("Hello world") == "Hello"
    first_word("a b c") == "a"
    first_word("Hi") == "Hi"
    first_word("") == ""
    """
    return s.split()[0]


def last_word(s):
    """
    Given a string of words separated by spaces, return the last word in the string. If the string is empty, return an empty string.
    
    Note:
    - There will always be at least one word in the string.
    - Assume that there are no leading or trailing spaces before or after the list of words.
    - Assume we use the universal newline character \n to separate lines.
    
    Examples:
    last_word("Hello world") == "world"
    last_word("a b c") == "c"
    last_word("Hi") == "Hi"
    last_word("") == ""
    """
    return s.split()[-1]


def middle_word(s):
    """
    Given a string of words separated by spaces, return the word at the middle of the string. If there is only one word in the string, return that word. If there is more than one word, return the word before last word if there is an even number of words. Return the word after last word if there is an odd number of words.
    
    Examples:
    middle_word("I like bananas") == "bananas"
    middle_word("I like coconuts") == "coconuts"
    middle_word("There are bananas") == "bananas"
    middle_