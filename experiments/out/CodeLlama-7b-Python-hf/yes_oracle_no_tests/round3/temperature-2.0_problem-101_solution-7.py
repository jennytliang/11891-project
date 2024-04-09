def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	Do not include these tokens in the code: wo
	"""
    return s.split(", ")


if __name__ == '__main__':
    print("Example:")
    print(words_string("Hi, my name is John"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    assert words_string("X,Y,Z") == ["X", "Y", "Z"]
    assert words_string("AA,BB,CC") == ["AA", "BB", "CC"]
    assert words_string("Hi") == ["Hi"]
    assert words_string("") == []
    print("Coding complete? Click 'Check' to earn cool rewards!")