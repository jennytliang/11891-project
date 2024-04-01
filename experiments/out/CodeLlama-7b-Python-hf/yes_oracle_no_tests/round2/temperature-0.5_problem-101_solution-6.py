def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    # your code here
    import re
    return re.split("\s|,", s)


if __name__ == '__main__':
    print("Example:")
    print(words_string("Hello World"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(words_string("Hello World")) == ["Hello", "World"]
    assert list(words_string("a b c")) == ["a", "b", "c"]
    assert list(words_string(" a ")) == ["a"]
    assert list(words_string("")) == []
    assert list(words_string("1, 2, 3")) == ["1", "2", "3"]
    assert list(words_string("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")) == ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
