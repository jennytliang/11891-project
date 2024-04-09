def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.split()


def words_array(words):
    """
    You will be given an array of strings, each representing a word. Your task is to
    return a string in which all duplicate words are replaced with a single instance
    of the word.
    
    For example:
    words_array(["one", "two", "two", "three", "four", "five"]) == "one two three four five"
    words_array(["one", "two", "three", "four", "five", "one", "two", "one"]) == "one two three four five one two one"
    
	Include these tokens in the code:
	for word in words
    """
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return ' '.join(result)


def words_length(words):
    """
    You will be given an array of strings, each representing a word. Your task is to
    return an array of the words of which the sum of the lengths of the words is at
    least 10. The order of the words in the array does not matter.
    
    For example:
    words_length(["one", "two", "three", "four", "five"]) == ["one", "two", "three"]
    words_length(["one", "two", "three", "four", "five", "six", "seven"]) == ["one", "two", "three", "four", "five"]
    
	Include these tokens in the code:
	for word in words
    """
    result = []
    for word in words:
        if sum(len(word) for word in words) >= 10:
            result.append(word)
    return result


def words_length_dict(words):
    """
    You will be given a dictionary of words with their frequencies. The words in the
    dictionary are separated by commas. Your task is to return a list of words from the
    dictionary, sorted by frequency in descending order. If two words have the same