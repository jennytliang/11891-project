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
    You will be given a sentence as a string.
    Return the first word in the sentence only if the first word is at least 4 characters long.
    Return the first word in the string s only if it is at least 4 characters long.
    Otherwise return "too short".
    
	For example:
	first_word("My name is John") == "My"
	first_word("Hi") == "too short"
    """

    return s.split()[0] if len(s.split()[0]) >= 4 else "too short"


def last_word(s):
    """
    You will be given a sentence as a string.
    Return the last word in the sentence only if the last word is at least 4 characters long.
    Return the last word in the string s only if it is at least 4 characters long.
    Otherwise return "too short".
    
	For example:
	last_word("My name is John") == "John"
	last_word("Hi") == "too short"
    """

    return s.split()[-1] if len(s.split()[-1]) >= 4 else "too short"


def middle_word(s):
    """
    You will be given a sentence as a string.
    If there is exactly one word in the sentence return "none".
    Otherwise return the middle word.
    
	For example:
	middle_word("My name is John") == "name"
	middle_word("Hi") == "none"
    """

    if len(s.split()) == 1:
        return "none"
    return s.split()[len(s.split()) // 2]


def reverse_words(s):
    """
    You will be given a sentence as a string.
    Reverse the order of the words in the sentence.
    
	For example:
	reverse_words("My name is John") == "John is name My"
    """
