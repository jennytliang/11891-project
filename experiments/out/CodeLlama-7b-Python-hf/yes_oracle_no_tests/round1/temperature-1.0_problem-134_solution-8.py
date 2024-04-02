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
    last_char = len(txt)-1
    
    if last_char == 1:
        return False
    else:
        for i in range(0,len(txt)):
            if txt[last_char]==' ':   
                return False
            elif txt[last_char].islower() or txt[last_char].isupper():
                return True
            else:
                return False
                
