def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	Do not include these tokens in the code: # s
	"""
    return s.replace(" ", ",").replace(",", " ").split()

print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))


def count_letters(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is to
    count the number of letters in each word and return an array of the counts.
    
    For example:
    count_letters("Hi, my name is John") == [2, 1, 4, 1, 5]
    count_letters("One, two, three, four, five, six") == [3, 3, 5, 4, 5, 3]
    
	Include these tokens in the code: words
	Do not include these tokens in the code: # s
	"""
    return [len(x) for x in s.replace(" ", ",").replace(",", " ").split()]

print(count_letters("Hi, my name is John"))
print(count_letters("One, two, three, four, five, six"))


def reverse_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is to
    reverse the order of the words and return them in the same format.
    
    For example:
    reverse_words("Hi, my name is John") == "John is name my Hi"
    reverse_words("One, two, three, four, five, six") == "six five four three two one"
    
	Include these tokens in the code: words
	Do not include these tokens in the code: # s
	"""
    return " ".join(s.replace(" ", ",").replace(",", " ").split()[::-1])

print(reverse_words("Hi, my name is John"))
print(reverse_words("One, two, three, four, five, six"))


def sum_of_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task