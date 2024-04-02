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


def even_lines(s):
    """
    You will be given a string of text separated by commas, periods and question marks. 
    Your task is to split the string into lines and return an array of only the even lines.
    
    For example:
    even_lines("Hi, my name is John, I am 26 years old., My favorite color is pink., I have 3 kids., I work as a teacher in the local school.") == ["My favorite color is pink.", "I have 3 kids."]
    even_lines("This, is, very, interesting.", ", ") == ["This", "interesting."]
    even_lines("This.", "This.") == ["This."]
    
	Include these tokens in the code: lines = ( s . split (", "
    """
    return s.split(", ")[1::2]


def count_substring(string, sub_string):
    """
    You will be given a string and a substring. 
    Write a function that returns the total occurrences of the substring in the 
    original string.
    
    For example:
    count_substring("aabcdefabc", "bc") == 2
    count_substring("aabcdefabc", "ab") == 2
    count_substring("aabcdefabc", "abc") == 2
    count_substring("aabcdefabc", "abcd") == 0
    count_substring("aabcdefabc", "") == 11
    count_substring("", "") == 0
    
	Include these tokens in the code: count = 0
    """
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i : i + len(sub_string)] == sub_string:
            count += 1
    return count


def string_splosion(s):
    """
    Write a function that receives a non-empty string and returns a string with 
    its first and last chars repeated one time each.
    
    For example:
