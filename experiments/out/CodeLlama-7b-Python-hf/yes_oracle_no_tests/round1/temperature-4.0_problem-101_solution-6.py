def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Do not include these tokens in the code: words = s . replace (" ","
	"""
    return s.split(" ")


def first_word(text):
    """
    You will be given a sentence as a string.
    Return the first word in the sentence only if the first word is in lower case.
    Otherwise return "Error".
    
    For example:
    first_word("This is my sentence.") == "This"
    first_word("This is my second sentence.") == "This"
    first_word("THIS IS MY SENTENCE.") == "Error"
    
    first_word("this is my sentence") == "Error"
    """
    return text.split(" ")[0] if text.split(" ")[0].islower() else "Error"


def fix_string(s):
    """
    You will be given a string.
    Return a string where all the characters that have a code number greater than 90
    are replaced with the character "*"
    
    For example:
    fix_string("abc") == "abc"
    fix_string("sA") == "s*"
    fix_string("Sb") == "*b"
    
    fix_string("aBc") == "aBc"
    fix_string("AbC") == "AbC"
    fix_string("aBc123") == "aBc****"
    """
    return "".join(["*" if ord(char) > 90 else char for char in s])


def first_repeat(s):
    """
    You will be given a string.
    If the string has 2 or more repeating characters, return the character repeated the most.
    Otherwise return "-1"
    
    For example:
    first_repeat("aabbbc") == "b"
    first_repeat("aabbcc") == "-1"
    first_repeat("aabbbccc") == "c"
    
    first_repeat("aabbccdd") == "b"
    first_repeat("aabbccdda") == "a"
    first_repeat("abcdea") == "a"
    """
    return max(set(s), key=s.