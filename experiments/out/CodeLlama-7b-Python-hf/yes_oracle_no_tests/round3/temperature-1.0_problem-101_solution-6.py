def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    words = s.replace(", "," ")
    return words.split()


def count_length(s):
    """
    You will be given a string of words separated by commas or spaces.
    Your task is to count the number of words in the string with a length of 4 or more.
    
    For example:
    count_length("Hi, my name is John") == 3
    count_length("One, two, three, four, five, six") == 3
    count_length("") == 0
    """
    s = s.replace(", ", " ")
    words = s.split()
    count = 0
    for word in words:
        if len(word) >= 4:
            count += 1
    return count


def no_punctuation(s):
    """
    You will be given a string.
    Your task is to remove any word that has punctuation in it.
    
    For example:
    no_punctuation("Hi, my name is John.") == "Hi my name is John"
    no_punctuation("This is a sentence without punctuation.") == "This is a sentence without punctuation"
    no_punctuation("No punctuation here!") == "No punctuation here"
    """
    punctuation = [".", ",", "?", "!", "'"]
    s = s.split()
    for word in s:
        for char in word:
            if char in punctuation:
                s.remove(word)
    return " ".join(s)


def no_vowels(s):
    """
    You will be given a string of words separated by commas or spaces.
    Your task is to return a list of words with all vowels removed.
    
    For example:
    no_vowels("Hi, my name is John") == ["Hi", "m", "n", "m", "n"]
    no_vowels("You are the best") == ["Yr", "r", "th", "th", "st"]
    no_vowels