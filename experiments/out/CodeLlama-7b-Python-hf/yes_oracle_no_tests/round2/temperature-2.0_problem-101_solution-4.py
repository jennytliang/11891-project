def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
	words = s.replace(", ", " ").split()
	return words


def count_substring(string, sub_string):
    """
    Count the number of occurrences of a substring in a string.
    
    For example:
    count_substring("Hello fellow earthlings!", "l") == 3
    count_substring("Hello fellow earthlings!", "ll") == 1
    """
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count


def difference_string(string1, string2):
    """
    Find the difference between two strings. The difference is calculated by the number of different characters in the
    two strings.
    
    For example:
    difference_string("hello", "hello") == 0
    difference_string("hello", "hel") == 1
    difference_string("hello", "hola") == 3
    """
    count = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count += 1
    return count


def check_brackets(string):
    """
    Check if brackets in the string are correctly placed.
    
    For example:
    check_brackets("(())") == True
    check_brackets("())(") == False
    """
    open_brackets = 0
    for i in range(len(string)):
        if string[i] == "(":
            open_brackets += 1
        elif string[i] == ")":
            if open_brackets > 0:
                open_brackets -= 1
            else:
                return False
    return open_brackets == 0


def reverse_string(string):
    """
    Reverse the order of the string's characters.
    
    For example:
    reverse_string("valor") == "rolav"
    """
    return string[::-1]

