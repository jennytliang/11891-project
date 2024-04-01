def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    return [item.strip() for item in s.split(',')]


def sum_positive(arr):
    """
    Given an array of integers. You need to find the sum of all the positive integers.
    
    sum_positive([1, 2, 3, 4, 5]) == 15
    """
