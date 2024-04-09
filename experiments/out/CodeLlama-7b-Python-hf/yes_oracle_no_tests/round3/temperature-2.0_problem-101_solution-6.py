def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	Do not include these tokens in the code: # Your code here
	"""
    return s.replace(", ", " ").split()


def first_word(s):
    """
    You will be given a sentence as a string.
    Return the first word in the string.
    
    For example:
    first_word("Once upon a time") == "Once"
    first_word("Hello, world!") == "Hello"
    first_word(" a word ") == "a"
    
	Include these tokens in the code: s[0]
	Do not include these tokens in the code: # Your code here
	"""
    return s.split()[0]


def last_word(s):
    """
    You will be given a sentence as a string.
    Return the last word in the string.
    
    For example:
    last_word("Once upon a time") == "time"
    last_word("Hello, world!") == "world"
    last_word(" a word ") == "word"
    
	Include these tokens in the code: s[-1]
	Do not include these tokens in the code: # Your code here
	"""
    return s.split()[-1]


def middle_word(s):
    """
    You will be given a sentence as a string.
    Return the middle word in the string. If there are two middle words, return the second one. If there are none, return "".
    
    For example:
    middle_word("Once upon a time") == "upon"
    middle_word("Hello, world!") == "world"
    middle_word(" a word ") == "word"
    middle_word("1,2,3,4,5") == ""
    middle_word(" one two three four five ") == "two"
    
	Include these tokens in the code: s[len(s)/2]
	Do not include these tokens in the code: # Your code here
	"""
    return s.split()[int(len(s.split()) / 2)]


def acronym(s):
    """
    You will be given an initialised string and a word dictionary.
    Capitalise