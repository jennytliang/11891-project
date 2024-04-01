def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    
	Include these tokens in the code: c 1 , c 2
	Do not include these tokens in the code: app les
	"""


    words = s.split("  ")
    apples = words[0][:-6]
    oranges = words[1][:-7]
    total = n
    
    total -= int(apples)
    total -= int(oranges)
    
    return total


def two_strings(s1,s2):
    """
    In this task, you will be given two strings. You should compare the strings and 
    find out whether any of the strings is a substring of the other.
    If is a substring return the string which is included in the other one.
    If the two strings are the same return the string itself.
    If none is a substring of the other return "NO".
    
    Note: A substring of a string is a part of the string that can be obtained by 
    removing some characters without changing the order of the rest of the characters.
    for examble:
    two_strings("hello","ll") -> "ll"
    two_strings("hello","lo") -> "lo"
    two_strings("hello","he") -> "he"
    two_strings("Awa","a") -> "a"
    two_strings("Awa","wa") -> "wa"
    two_strings("Awa","A") -> "A"
    """

    if s1 in s2:
        return s1
    elif s2 in s1:
        return s2
    else:
        return "NO"

def string_repeater(s,n):
    """
    In this task, you should return a string which is n copies of the s parameter.
    for examble:
    string_repeater("aa", 3) -> "aaaa"
    string_repeater("baa", 2) -> "baaa"
    string_repeater("aaaa", 1) -> "aaaa"
    """

    return s * n

def string_reverser(s):
    """
    In this task, you should return a string which is a reverse order of the s parameter.
    for examble:
    string_reverser("hello") -> "olleh"
    string_reverser("edab