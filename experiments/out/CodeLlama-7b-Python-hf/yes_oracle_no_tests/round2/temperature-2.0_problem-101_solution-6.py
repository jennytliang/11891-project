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
    # Your code here
    return s.split(", " if "," in s else " ")


# 2. Words Count
def words_count(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to count the occurrences of each word and return a dictionary with the words as
    keys and their counts as values.
    
    For example:
    words_count("Hi, my name is John, my name is John") == {"my": 2, "name": 2, "Hi": 1, "John": 2}
    words_count("One, two, three, four, five, six, one, one, two, three") == {"three": 2, "one": 3, "two": 2, "four": 1, "five": 1, "six": 1}
    
    Hint:
    Use words_string method to get the words array.
    
	Include these tokens in the code: words = ( s
	Do not include these tokens in the code: return
	"""
    # Your code here
    words = s.split(", " if "," in s else " ")
    words_dict = {}
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict


# 3. Words Unique Count
def words_unique_count(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to count the unique words in that string, excluding all duplicates.
    
    For example:
    words_unique_count("Hi, my name is John, my name is John") == 3
    words_unique_count("One, two, three, four, five, six, one, one, two, three") == 4
    
    Hint:
    Use words_count method to get the words dictionary.
    
	Include these tokens in the code: words = ( s
	Do not include these tokens in the code: return
	