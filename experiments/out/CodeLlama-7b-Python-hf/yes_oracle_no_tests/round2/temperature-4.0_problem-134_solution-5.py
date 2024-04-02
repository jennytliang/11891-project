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
    
	Include these tokens in the code: if len ( txt ) ==
	'''
    if len (txt) == 0:
        return False
    if txt[-1].isalpha():
        return False
    else:
        return True

#check_if_last_char_is_a_letter("apple pie") #➞ False
#check_if_last_char_is_a_letter("apple pi e") #➞ True
#check_if_last_char_is_a_letter("apple pi e ") #➞ False
#check_if_last_char_is_a_letter("") #➞ False 

def check_if_last_char_is_a_number(txt):
    '''
    Create a function that returns True if the last character
    of a given string is a digit and is not a part of a word,
    and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_number("apple pie") ➞ False
    check_if_last_char_is_a_number("apple pi e") ➞ False
    check_if_last_char_is_a_number("apple pi e ") ➞ False
    check_if_last_char_is_a_number("") ➞ False 
    
	Include these tokens in the code: if len ( txt ) ==
	'''
    if len (txt) == 0:
        return False
    if txt[-1].isdigit():
        return False
    else:
        return True

#check_if_last_char_is_a_number("apple pie") #➞ False
#check_if_last_char_is_a_number("apple pi e") #➞ False
#check_if_last_char_is_a_number("apple pi e ") #➞ False
#check_if_last_char_is_a_number("") #➞ False 

def check_if_last_char_is_a_letter_or_number(txt):
    '''
    Create a function that returns True