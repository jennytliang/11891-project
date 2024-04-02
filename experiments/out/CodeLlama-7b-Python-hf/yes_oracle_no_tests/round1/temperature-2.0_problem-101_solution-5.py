def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.replace(", ", " ").split(" ")


def count_substring(string, sub_string):
    """
    Write a function that takes a string and a substring.
    It returns the start index of the first occurrence of the substring in the string,
    or -1 if there is no occurrence of the substring in the string.
    
    For example:
    count_substring("lolabcabcabc", "abc") == 3
    count_substring("lolabcabcabc", "d") == -1
    
    Hint: Use count method.
    """
    return string.count(sub_string)


def string_splosion(str):
    """
    Write a function called string_splosion that takes a non-empty string as a parameter.
    Without using any string methods, write a function that returns a new string that
    goes from the zeroth index up to but not including the last index.
    
    For example:
    string_splosion("code") # returns "c", "co", "cod"
    """
    result = ""
    for i in range(len(str)):
        result += str[:i]
    return result


def last_survivor(letters, coords):
    """
    You will be given a word, a 2D grid of letters and a list of locations of the
    same length. The locations will be where the word should start and end.
    Return the word from the grid.
    
    For example:
    letters = "abcde"
    coords = [[0, 2], [0, 3], [2, 0], [2, 1], [2, 2]]
    returns "bcde"
    """
    result = ""
    for coord in coords:
        x, y = coord
        result += letters[y]
    return result


def array_diff(input_array, num):
    """
    Given an array and a number, return a new array containing each element in the
    input array except the number passed.
    
    For example:
    array_diff([1, 2, 