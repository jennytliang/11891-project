def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.replace(", "," ").split(" ")


def count_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to count the occurrences of each word in the string and return an object
    containing the word and count.
    
    For example:
    count_words("Hi, my name is John") == {"Hi": 1, "my": 1, "name": 1, "is": 1, "John": 1}
    count_words("a, a, b, b, b") == {"a": 2, "b": 3}
    
    The string will not contain punctuation, only letters and commas/spaces
    """
    words = s.replace(", ", " ").split(" ")
    return {word: words.count(word) for word in words}


def sort_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to sort the words in the string in ascending order based on the sum of their
    letters' Unicode values and return the result as a string with words separated
    by commas.
    
    For example:
    sort_words("one, two, three") == "one, three, two"
    sort_words("one two, three") == "one, three, two"
    
    The string will not contain punctuation, only letters and commas/spaces
    """
    words = s.replace(", ", " ").split(" ")
    return ", ".join(sorted(words, key=lambda word: sum([ord(c) for c in word])))


def sort_words_case_insensitive(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to sort the words in the string in ascending order based on the sum of their
    letters' Unicode values, but ignore the casing of the words.
    
    For example:
    sort_words_case_insensitive("dot, Dot, OT, oT, OT, Dot