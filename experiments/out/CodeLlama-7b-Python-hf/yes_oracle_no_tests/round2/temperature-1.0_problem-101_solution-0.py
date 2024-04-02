def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	"""
    return s.split()


def fix_string(s):
    """
    You will be given a string with words separated by commas, dots or semicolons. You should
    fix the string by removing all the extra characters (spaces, tabs, newlines) from the start
    and the end of the string, and from between the words.
    
    For example:
    fix_string("   a, b; c  ") == "a, b; c"
    fix_string("   a, b; c  d") == "a, b; c d"
    fix_string("   a, b; c  d  ") == "a, b; c d"
    fix_string("a,   b; c  d  ") == "a, b; c d"
    
	Include these tokens in the code: spaces, tabs, newlines
	"""
    return s.strip().replace(',', '').replace(';', '').replace('.', '')


def first_word(s):
    """
    You will be given a string of words separated by commas, semi-colons or spaces.
    You should return the first word in the string.
    
    For example:
    first_word("Hello, world!") == "Hello"
    first_word("Hello world!") == "Hello"
    first_word("Hello   world!") == "Hello"
    first_word("Hello; world!") == "Hello"
    first_word(" Hello   world!") == "Hello"
    
	Include these tokens in the code: spaces, tabs, newlines
	"""
    return s.split()[0]


def remove_characters(s, n):
    """
    You will be given a string of words separated by commas, dots or spaces. You should remove
    all occurrences of n-th character in the string and return a new string.
    
    For example:
    remove_characters("Hello", 0) == "eHll"
    remove_characters("Hello", 1) == "Hllo"
    remove_characters("Hello", 2) == "