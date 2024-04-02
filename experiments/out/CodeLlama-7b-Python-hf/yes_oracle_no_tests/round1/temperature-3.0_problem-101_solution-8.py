def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    # your code here


def first_word(s):
    """
    You will be given a sentence as a string. Your task is to return the first word 
    in the sentence.
    
    For example:
    first_word("one two three") == "one"
    first_word("Hello world!") == "Hello"
    first_word("!hello world") == "!"
    
	Include these tokens in the code: first = s . split ( " " ) [0]
	"""
    # your code here


def last_word(s):
    """
    You will be given a sentence as a string. Your task is to return the last word 
    in the sentence.
    
    For example:
    last_word("one two three") == "three"
    last_word("Hello world!") == "world"
    last_word("How are you?") == "you"
    
	Include these tokens in the code: last = s . split ( " " ) [-1]
	"""
    # your code here


def middle_word(s):
    """
    You will be given a sentence as a string. Your task is to return the middle word(s) 
    in the sentence.
    
    For example:
    middle_word("one two three") == "two"
    middle_word("Hello world!") == "world"
    middle_word("one two three four") == "two three"
    
	Include these tokens in the code: words = s . split ( " " )
	"""
    # your code here


def acronym(s):
    """
    You will be given an abbreviated word as a string. Your task is to return its 
    acronym.
    
    For example:
    acronym("USA") == "U.S.A."
    acronym("Indonesia") == "I.N.D.N."
    
	Include these tokens in the code: acronym = ""
	"""
    # your code here


def tokenize(s):
    """
    You will be