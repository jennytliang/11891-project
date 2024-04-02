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
    return True if len(txt) > 0 and txt[-1] not in "abcdefghijklmnopqrstuvwxyz" else False


#print(check_if_last_char_is_a_letter("apple pie")) #➞ False
#print(check_if_last_char_is_a_letter("apple pi e")) #➞ True
#print(check_if_last_char_is_a_letter("apple pi e ")) #➞ False
#print(check_if_last_char_is_a_letter("")) #➞ False


def check_if_first_char_is_a_letter(txt):
    '''
    Create a function that returns True if the first character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_first_char_is_a_letter("apple pie") ➞ False
    check_if_first_char_is_a_letter("apple pi e") ➞ False
    check_if_first_char_is_a_letter("apple pi e ") ➞ True
    check_if_first_char_is_a_letter("") ➞ False
    
	Include these tokens in the code: if len ( txt ) ==
    '''
    return True if len(txt) > 0 and txt[0] not in "abcdefghijklmnopqrstuvwxyz" else False


#print(check_if_first_char_is_a_letter("apple pie")) #➞ False
#print(check_if_first_char_is_a_letter("apple pi e")) #➞ False
#print(check_if_first_char_is_a_letter("apple pi e ")) #➞ True
#print(check_if_first_char_is_a_letter("")) #➞ False


def check_if_word_is_palindrome(