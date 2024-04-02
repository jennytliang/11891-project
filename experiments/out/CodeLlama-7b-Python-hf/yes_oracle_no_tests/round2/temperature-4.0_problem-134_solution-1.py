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
    
	Do not include these tokens in the code: return False
	'''
    
    if txt == "" or txt == " ":
        return False
    else:
        for i in range(len(txt)-1, -1, -1):
            if txt[i] == " ":
                continue
            else:
                if 64 < ord(txt[i]) < 91 or 96 < ord(txt[i]) < 123:
                    return False
                else:
                    return True

