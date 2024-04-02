def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    
	Include these tokens in the code: if
	Do not include these tokens in the code: last _ char =
	'''

    if len(txt) == 0:
        return False

    # remove whitespace
    txt = txt.replace(' ', '')
    
    # check to see if last char is an alpha char
    if txt[-1].isalpha():
        return False
    else:
        return True

