def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
	words = s.replace(",", " ").split(" ")
	return words


def first_word(s):
    """
    You will be given a sentence as a string.
    Return the first word in the sentence.
    
    For example:
    first_word("Hello world") == "Hello"
    first_word("a b c d e") == "a"
    """
    word = s.split(" ")[0]
    return word


def last_word(s):
    """
    You will be given a sentence as a string.
    Return the last word in the sentence.
    
    For example:
    last_word("Hello world") == "world"
    last_word("a b c d e") == "e"
    """
    word = s.split(" ")[-1]
    return word


def middle_word(s):
    """
    You will be given a sentence as a string.
    Return the middle word in the sentence. If there are two middle words, return the second one.
    
    For example:
    middle_word("Hello world") == "world"
    middle_word("a b c d e") == "c"
    middle_word("One two three four five six") == "four"
    """
    words = s.split(" ")
    if len(words) % 2 == 0:
        return words[len(words) // 2 - 1]
    else:
        return words[len(words) // 2]


def acronym(s):
    """
    You will be given a sentence as a string.
    Return the acronym of the sentence.
    
    For example:
    acronym("Health, Education and Welfare") == "HEW"
    acronym("Knowledge is power") == "KE"
    acronym("Science and Technology") == "ST"
    """
    return "".join([word[0] for word in s.split(" ")])


def short_word(s):
    """
    You will be given a sentence as a string.