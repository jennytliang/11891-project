def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""

    # s = s.replace(', ', ' ')
    # s = s.split()
    # return s

    # return s.split(', ')
    return s.replace(', ', ' ').split()


def first_word(s):
    """
    You will be given a sentence and you will need to return the first word in the sentence.
    
    For example:
    first_word("Hello world") == "Hello"
    first_word("a b c d e") == "a"
    
    You may need to use the .split() method to split the sentence into words.
    """

    return s.split()[0]


def last_word(s):
    """
    Given a string of words separated by spaces, return the last word in the string.
    
    Your solution should only have a single call to .split().
    """

    return s.split()[-1]


def middle_word(s):
    """
    Given a string of words separated by spaces, return the middle word.
    
    If there is more than one middle word, return the first one.
    If there are no middle words, return "".
    
    Assume that there will always be at least one word in s.
    
    Examples:
    middle_word("Hello world") == "world"
    middle_word("Testing") == "Testing"
    middle_word("One two three four") == "two"
    middle_word("Hello World") == "World"
    """

    return s.split()[len(s.split()) // 2]


def reverse_words(s):
    """
    Given a string of words separated by spaces, return a string with the words in reverse order.
    
    For example:
    reverse_words("Hello world") == "world Hello"
    reverse_words("Testing") == "Testing"
    reverse_words("One two three four") == "four three two One"
    reverse_words("Hello World") == "World Hello"
    """

    return ' '.join(reversed(s.split()))


def