def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    words = s.replace(", ", " ").split(" ")
    return words


def reverse_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is to
    reverse the string word by word.
    
    For example:
    reverse_words("Hi, my name is John") == "John is name my Hi"
    reverse_words("One, two, three, four, five, six") == "six five four three two one"
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    words = s.replace(", ", " ").split(" ")
    return " ".join(reversed(words))


def count_words(s, w):
    """
    You will be given a string of words separated by commas or spaces. Your task is to
    count the occurrences of each word in the string and return a string with each word
    and its count.
    
    For example:
    count_words("Hi, my name is John", "my") == "my (2)"
    count_words("One, two, three, four, five, six", "one") == "one (1)"
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    words = s.replace(", ", " ").split(" ")
    return f"{w} ({words.count(w)})"


def find_longest_word(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is to
    find the longest word in the string and return it.
    
    For example:
    find_longest_word("Hi, my name is John") == "John"
    find_longest_word("One, two, three, four, five, six") == "six"
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    words = s.replace(", ", " ").split(" ")
    return max(words, key=len)

