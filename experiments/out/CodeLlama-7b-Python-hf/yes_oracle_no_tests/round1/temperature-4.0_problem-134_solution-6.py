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
    
    if len(txt)==0:
        return False
    
    if len(txt)==1:
        if txt[0].isalpha():
            return False
        else:
            return True
    
    if txt[-1].isalpha():
        if txt[-2] == " ":
            return False
        else:
            return True
    else:
        return False

def check_if_last_char_is_a_letter_2(txt):
    if len(txt) > 1:
        return txt[-2] != " " and txt[-1].isalpha()
    if len(txt) == 1:
        return not txt[0].isalpha()
    return False

check_if_last_char_is_a_letter("apple pie") #➞ False
#check_if_last_char_is_a_letter("apple pi e") #➞ True
#check_if_last_char_is_a_letter("apple pi e ") #➞ False
#check_if_last_char_is_a_letter("") #➞ False