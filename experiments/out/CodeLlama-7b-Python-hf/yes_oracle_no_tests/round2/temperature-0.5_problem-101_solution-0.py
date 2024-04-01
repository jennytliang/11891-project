def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    words = s.replace (', ', ' ').split ()
    return words


def count_letters(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to count the number of letters in the string.
    
    For example:
    count_letters("Hi, my name is John") == 10
    count_letters("One, two, three, four, five, six") == 30
    
	Include these tokens in the code:
	length = len (s . replace (", ", " "))
	"""
    length = len(s.replace(', ', ' '))
    return length


def count_sentences(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to count the number of sentences in the string.
    
    For example:
    count_sentences("Hi, my name is John") == 1
    count_sentences("One, two, three, four, five, six") == 1
    count_sentences("One. Two, three; four: five? six!") == 5
    
	Include these tokens in the code:
	sentences = s . split (".")
	"""
    sentences = s.split('.')
    return len(sentences)


def count_letters_digits(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to count the number of letters and digits in the string.
    
    For example:
    count_letters_digits("Hi, my name is John") == 10
    count_letters_digits("One, two, three, four, five, six") == 30
    count_letters_digits("One, two, three, four, five, six, 1, 2, 3") == 17
    
	Include these tokens in the code:
	letters = len (s . replace (", ", " "))
	digits = len (s . replace (", ", " "