def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s
	Do not include these tokens in the code: return
	"""
    words = s.replace(" ", ",")
    words = words.split(",")
    return words


#print(words_string("Hi, my name is John"))
#print(words_string("One, two, three, four, five, six"))

def reverse_words(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is to
    reverse the order of the words.
    
    For example:
    reverse_words("Hi, my name is John") == "John is name my Hi"
    reverse_words("One, two, three, four, five, six") == "six five four three two one"
    
    Do not include these tokens in the code: words = ( s
    Include these tokens in the code: return
    """
    words = s.replace(" ", ",")
    words = words.split(",")
    words.reverse()
    words = ", ".join(words)
    return words


#print(reverse_words("Hi, my name is John"))
#print(reverse_words("One, two, three, four, five, six"))

def reverse_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is to
    reverse the order of the words while keeping the commas and spaces.
    
    For example:
    reverse_string("Hi, my name is John") == "John is name my, Hi"
    reverse_string("One, two, three, four, five, six") == "six five four three two one,"
    
    Do not include these tokens in the code: words = ( s
    Include these tokens in the code: return
    """
    words = s.replace(" ", ",")
    words = words.split(",")
    words.reverse()
    words = ", ".join(words)
    return words


#print(reverse_string("Hi, my name is John"))
#print(reverse_string("One, two, three, four, five, six"))

def count_substring(string, sub_string):
    """
    You will be given