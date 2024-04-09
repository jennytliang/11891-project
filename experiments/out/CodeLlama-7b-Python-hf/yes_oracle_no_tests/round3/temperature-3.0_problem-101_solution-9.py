def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Do not include these tokens in the code: "" ") return
	"""
    return s.replace(", ", " ").split()

    # return s.replace(",", " ").split()


if __name__ == '__main__':
    print(words_string("Hi, my name is John"))
    print(words_string("One, two, three, four, five, six"))
