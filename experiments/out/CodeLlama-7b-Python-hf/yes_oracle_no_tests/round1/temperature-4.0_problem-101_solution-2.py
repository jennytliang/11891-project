def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: ( s
	"""

    wo = s.split(",")
    w = []
    for i in wo:
        w.append(i.strip())
    return w
    
    # return s.split(",")


if __name__ == '__main__':
    print("Example:")
    print(words_string("Hello, world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_string("Hello, world") == ['Hello', 'world']
    assert words_string(" a, b") == ['a', 'b']
    assert words_string(" a b") == ['a', 'b']
    assert words_string(" a, b, c") == ['a', 'b', 'c']
    assert words_string(" a, b, c, ") == ['a', 'b', 'c']
    assert words_string("Hi, my name is John") == ['Hi', 'my', 'name', 'is', 'John']
    assert words_string("One, two, three, four, five, six") == ['One', 'two', 'three', 'four', 'five', 'six']
    print("Coding complete? Click 'Check' to earn cool rewards!")
