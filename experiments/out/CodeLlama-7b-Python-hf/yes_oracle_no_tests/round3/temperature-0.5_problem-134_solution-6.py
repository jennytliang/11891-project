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
    #code goes here
    if len(txt) == 0:
        return False
    elif txt[-1].isalpha() == True:
        return True
    else:
        return False

#check_if_last_char_is_a_letter("apple pie") #, False)
#check_if_last_char_is_a_letter("apple pi e") #, True)
#check_if_last_char_is_a_letter("apple pi e ") #, False)
#check_if_last_char_is_a_letter("") #, False)
#check_if_last_char_is_a_letter("a") #, False)
#check_if_last_char_is_a_letter("a ") #, False)
#check_if_last_char_is_a_letter("a b") #, False)
#check_if_last_char_is_a_letter("a b ") #, False)
#check_if_last_char_is_a_letter("a b c") #, False)
#check_if_last_char_is_a_letter("a b c ") #, False)
#check_if_last_char_is_a_letter("a b c d") #, False)
#check_if_last_char_is_a_letter("a b c d ") #, False)
#check_if_last_char_is_a_letter("a b c d e") #, True)
#check_if_last_char_is_a_letter("a b c d e ") #, False)
#check_if_last_char_is_a_letter("a b c d e f") #, True)
#check_if_last_char_is_a_letter("a b c d e f ") #, False)
#check_if_last_char_is_a_letter("a b c d e f g") #, True)
#check_if_last_char_is_a_letter("a b c d e f g ") #, False)
#check_if_last_char_is_