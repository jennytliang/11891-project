def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    s_array = s.replace(",", " ").split()
    return list(s_array)

if __name__ == '__main__':
    print("Example with \"Hi, my name is\" string: " + str(words_string("Hi, my name is")))
