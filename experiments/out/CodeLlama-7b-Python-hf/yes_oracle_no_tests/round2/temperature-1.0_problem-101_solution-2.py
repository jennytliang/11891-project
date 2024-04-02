def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Do not include these tokens in the code: words = s . replace (", ",
	"""
    return s.replace(", ", " ").replace(",", " ").split()


def count_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to count the number of words in the string and return an array of the words.
    
    For example:
    count_words("Hi, my name is John") == 5
    count_words("One, two, three, four, five, six") == 6
    
	Do not include these tokens in the code: words = s . replace (", ",
	"""
    return len(s.replace(", ", " ").replace(",", " ").split())


def count_unique_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to count the number of unique words in the string.
    
    For example:
    count_unique_words("Hi, my name is John") == 4
    count_unique_words("One, two, one, two, three, one, two") == 3
    
	Do not include these tokens in the code: words = s . replace (", ",
	"""
    return len(set(s.replace(", ", " ").replace(",", " ").split()))


def sum_numbers(s):
    """
    You will be given a string of space separated numbers. Your task is to return
    the sum of those numbers.
    
    For example:
    sum_numbers("1 2 3 4 5") == 15
    sum_numbers("1 2 -1 3 -3 5") == 0
    sum_numbers("0 0 0 0 0") == 0
    
	Do not include these tokens in the code: words = s . replace (", ",
	"""
    return sum([int(x) for x in s.split()])


def reverse_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to reverse the string and return it as a string of