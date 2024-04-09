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
    
    if txt == "":
        return False
    elif len(txt) == 1:
        if txt[0].isalpha():
            return False
        else:
            return True
    else:
        for i in range(len(txt)-1,0,-1):
            if txt[i].isalpha():
                if txt[i-1] == " ":
                    return True
                else:
                    return False
            else:
                continue
            
def check_if_last_char_is_a_letter_2(txt):
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
    
    if txt == "":
        return False
    elif len(txt) == 1:
        if txt[0].isalpha():
            return False
        else:
            return True
    else:
        for i in range(len(txt)-1,0,-1):
            if txt[i].isalpha():
                if txt[i-1] != " ":
                    return True
                else:
                    return False
            else:
                continue
            
def check_if_last_char_is_a_letter_3(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.