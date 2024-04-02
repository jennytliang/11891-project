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
    
    if txt=="":
        return False
    elif ' ' in txt:
        for ltrs in txt[:-1].split(' '):
            if ord(ltrs[-1]) < ord('a'):
                if ord(ltrs[-1]) < ord('A'):
                    return False  
                    break
        if ord(txt[-1]) < ord('a') and ord(txt[-1]) < ord('A'):
            return False
        else:
            return True
    elif txt[0]==' ' and txt[-1]==' ':
        txt=txt[1:-1]
        if ord(txt[-1]) > ord('a') and ord(txt[-1]) < ord('A'):
            return False
        elif ord(txt[-1]) > ord('a') and ord(txt[-1]) > ord('5'):
            return False
        else:
            return True
    elif txt[-1]==' ':
        txt=txt[:-1]
        if ord(txt[-1]) > ord('a') and ord(txt[-1]) < ord('A'):
            return False
        elif ord(txt[-1]) > ord('a') and ord(txt[-1]) > ord('5'):
            return False
        elif ord(txt[-1])=='.' or ord(txt[-1])==':' or ord(txt[-1])=='?' or ord(txt[-1])=='!':
            return False
        else:
            return True
    else:
        return False

#print(check_if_last_char_is_a_letter("apple pi e "))
#print(check_if_last_char_is_a_letter("apple pie"))
#print(check_if_last_char_is_a_letter("apple pi e"))
#print(check_if_last_char_is_a_letter("apple pi e."))
#print(check_if_last_char_is_a_letter("apple pi e."))
print(check_if_last_char_is_a_letter(""))