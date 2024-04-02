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
    return s.replace(',', ' ').replace(',', ' ').split()


def count_words(s, w):
    """
    You will be given two strings. The first string will contain multiple words separated by spaces. The second string will be a single word. Your task is to count how many times the second word appears in the first string.

    For example:
    count_words("hi world hi", "hi") == 2
    count_words("hi world hi", "world") == 1
    """
    # your code here
    return s.split().count(w)


def count_substring(string, sub_string):
    """
    Given a string, find the number of times that the string appears in it as a substring.

    string_count("ABCDCDC", "CDC") == 2
    string_count("hello world", "l") == 3
    string_count("AAAAA", "AAAA") == 1
    string_count("mississippi", "issi") == 2
    """
    # your code here
    return string.count(sub_string)


def check_brackets(s):
    """
    You will be given a string of brackets and you will need to return whether or not they are balanced.

    Input: String of brackets
    Output: Boolean
    """
    # your code here
    stack = []
    for char in s:
        if char == '{' or char == '[' or char == '(':
            stack.append(char)
        elif char == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False
        elif char == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
        elif char == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
    return len(stack) == 0


def sum_digits(s):
    """
    You will be given a string of numbers. You must return the sum of all the numbers