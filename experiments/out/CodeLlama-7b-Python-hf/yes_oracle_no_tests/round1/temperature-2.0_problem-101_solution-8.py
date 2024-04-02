def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    words = s.replace(", ", " ")
    return words.split(" ")


def is_palindrome(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is to
    check each word for palindromes and create an array of palindromes.

    For example:
    is_palindrome("One, two, three, four, five, six") == ["One", "two", "three", "six"]
    is_palindrome("Lucky, numbers, are, multiplied, by, the, big, number") == ["Lucky", "numbers", "big", "number"]

    Note: A palindrome is a word that is spelled the same backward and forward.
    """
    words = s.replace(", ", " ")
    result = []
    for word in words.split(" "):
        if is_palindrome_word(word):
            result.append(word)
    return result


def is_palindrome_word(s):
    return s == s[::-1]


def is_palindrome_word_v2(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is to
    check each word for palindromes and create an array of palindromes.

    For example:
    is_palindrome_word_v2("One, two, three, four, five, six") == ["One", "two", "three", "six"]
    is_palindrome_word_v2("Lucky, numbers, are, multiplied, by, the, big, number") == ["Lucky", "numbers", "big", "number"]

    Note: A palindrome is a word that is spelled the same backward and forward.
    """
    return s == s[::-1]


def is_palindrome_word_v3(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is to
    check each word for palindromes and create an array of pal