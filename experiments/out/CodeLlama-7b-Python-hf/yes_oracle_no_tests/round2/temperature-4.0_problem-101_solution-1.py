def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	Do not include these tokens in the code: wo
	"""
    return s.replace(" ", ",").split(",")


def remove_empty_words(words):
    """
    You will be given an array of strings as the first argument. You should remove 
    the empty strings from the array and return an array of the remaining words.
    
    For example:
    remove_empty_words(["Hi", "my", "", "name", "is", "John", ""]) == ["Hi", "my", "name", "is", "John"]
    remove_empty_words(["Hi", "my", "name", "is", "John", ""]) == ["Hi", "my", "name", "is", "John"]
    
	Include these tokens in the code: words
	Do not include these tokens in the code: wo
    """
    return [word for word in words if word]


def reverse_string(string):
    """
    You will be given a string as the first argument. You should return a string 
    with all the characters of the original string in reverse order.
    
    For example:
    reverse_string("Hi my name is John") == "hnoinema ym iH"
    reverse_string("Hello world!") == "!dlrow olleH"
    
	Include these tokens in the code: string, reverse
	Do not include these tokens in the code: reverse
    """
    return string[::-1]


def reverse_string_in_place(string):
    """
    You will be given a string as the first argument. You should return the same string, 
    but with all the characters of the original string in reverse order.
    
    For example:
    reverse_string_in_place("Hi my name is John") == "hnoinema ym iH"
    reverse_string_in_place("Hello world!") == "!dlrow olleH"
    
	Include these tokens in the code: string, reverse
	Do not include these tokens in the code: reverse
    """
    return "".join(reversed(string))


def remove_exclamation_marks(string):
    """
    You will be given