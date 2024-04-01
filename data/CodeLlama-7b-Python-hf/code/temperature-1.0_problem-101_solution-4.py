def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    return s.replace(',', ' ').split()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(words_string("Hi, my name is John")) == ['Hi', 'my', 'name', 'is', 'John'], "First"
    assert list(words_string("One, two, three, four, five, six")) == ['One', 'two', 'three', 'four', 'five', 'six'], "Second"
    assert list(words_string("One two three four five six")) == ['One', 'two', 'three', 'four', 'five', 'six'], "Third"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
