def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.replace(", ", " ").split()


def unique_list(l):
    """
    Return a list of unique elements in l.
    
    For example:
    unique_list([1, 3, 5, 3, 7, 5, 1, 9]) == [1, 3, 5, 7, 9]
    unique_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    unique_list([1, 2, 2, 3, 4, 4, 4, 5]) == [1, 2, 3, 4, 5]
    
    You can only use the following Python built-in methods:
    + list
    + max
    + min
    + sorted
    + sum
    """
    return list(set(l))


def string_to_list(s):
    """
    You will be given a string s containing zero or more words separated by whitespace. 
    Your task is to create a list of strings containing each word from s.
    
    For example:
    string_to_list("Hi my name is John") == ["Hi", "my", "name", "is", "John"]
    string_to_list("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    string_to_list("Hi, my name is John, how are you?") == ["Hi", "my", "name", "is", "John", "how", "are", "you?"]
    
    You can only use the following Python built-in methods:
    + list
    + max
    + min
    + sorted
    + sum
    """
    return s.split()


def list_to_string(l):
    """
    You will be given a list of strings l. Your task is to return a string containing all the words in l 
    concatenated into one string with each word separated by a comma and a space.
    
    For example:
    list_to_