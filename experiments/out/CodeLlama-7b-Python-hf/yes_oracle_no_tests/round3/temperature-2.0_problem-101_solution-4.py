def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	"""
    # Your code here
    
    return s.split()


def reverse_string(s):
    """
    You will be given a string. Reverse the string and return it as a new string.
    
    For example:
    reverse_string("Hi") == "iH"
    reverse_string("Here") == "ereH"
    """
    # Your code here
    
    return s[::-1]


def remove_char(s, index, times):
    """
    You will be given two integers and a string.
    Using these integers and the string data, you need to remove characters from the string.
    
    The first integer denotes the index location of the character that you need to remove.
    The second integer denotes how many characters you need to remove.
    
    If the optional third parameter (k) is provided, it will denote that after removing the
    characters you must remove every kth character from the string, starting with the character at index location i.
    
    Return the final string after all operations.
    
    For example:
    remove_char("This is a string", 8, 3, 2) == "Thsa string"
    remove_char("This is a string", 8, 2) == "Thsa string"
    remove_char("This is a string", 1, 4) == "Ths string"
    remove_char("This is a string", 0, 12) == ""
    
    NOTE: An invalid input will be treated as a 0-argument function and will return "Invalid input".
    """
    # Your code here
    
    if index > len(s) or times > len(s) or times < 0 or index < 0:
        return "Invalid input"
    
    return s[:index] + s[index + times:]


def reverse_every_n_char(s, n):
    """
    You will be given a string and a number n.
    Your task is to reverse every n characters of the string.
    
    If the string's length is not a multiple of n, left-out characters at the end of the string