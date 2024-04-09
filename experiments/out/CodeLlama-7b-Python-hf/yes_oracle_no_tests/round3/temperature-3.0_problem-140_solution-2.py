def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ans = text for i in range (
	"""
    ans = text
    for i in range(len(text)):
        if text[i] == " ":
            ans = ans.replace(text[i], "_")
    return ans


def remove_punctuation(text):
    """
    Given a string text, remove all punctuation in it, 
    and return the same text without punctuation 
    
    remove_punctuation("Example.") == "Example"
    remove_punctuation("Test?") == "Test"
    remove_punctuation("Huh!") == "Huh"
    
    Include these tokens in the code: 
    punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    """
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    for i in range(len(text)):
        if text[i] in punctuation:
            text = text.replace(text[i], "")
    return text


def remove_digits(text):
    """
    Given a string text, remove all digits in it, 
    and return the same text without digits 
    
    remove_digits("12345") == "12345"
    remove_digits("abc123def") == "abcdef"
    remove_digits("123abc456") == "abc"
    
    Include these tokens in the code: 
    digits = "0123456789"
    """
    digits = "0123456789"
    for i in range(len(text)):
        if text[i] in digits:
            text = text.replace(text[i], "")
    return text


def remove_vowels(text):
    """
    Given a string text, remove all vowels in it, 
    and return the same text without vowels 
    
    remove_vowels("abcde")