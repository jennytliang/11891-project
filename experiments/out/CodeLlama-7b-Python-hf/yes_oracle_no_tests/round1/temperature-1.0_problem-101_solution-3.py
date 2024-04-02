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
    You will be given a string and a substring.
    Count in how many occurrences the substring,
    also known as the subsequence, shows up in the original string.
    
	Example:
    count_substring("abaabca", "ab") == 2
    count_substring("code", "cod") == 1
    count_substring("aaa", "a") == 3
    
    The subsequence can be of any length (incl. `0` - empty string).
    However, it must be contained inside the initial string.
    
    If there are no occurrences, return `0`.
    """
    return string.count(sub_string)


def string_splosion(string):
    """
    Write a function that receives a non-empty string and an integer `n`.
    The function should return the `n`-th substring of the input string.
    
	The first substring is the string itself.
	The second substring is the string with the first and the last character removed.
	The third substring is the string with every second character removed.
	The `nth` substring follows a similar pattern.
    
    Examples:
    string_splosion('Code', 2) == 'od'
    string_splosion('Code', 3) == 'e'
    string_splosion('Code', 1) == 'Code'
    
    If `n` is greater than the length of the string, return an empty string `''`.
    The `n` will always be greater than or equal to `0`.
    The string length will always be greater than `0`.
    """
    return string[:n]


def last_survivor(letters, coords):
    """
    Imagine that you are building a long wall that is `letters` characters long.
    You will be given some `coords` to fill in some of the wall with stones.
    Each stone has a width of `1` character and you want to make sure that there
    are no