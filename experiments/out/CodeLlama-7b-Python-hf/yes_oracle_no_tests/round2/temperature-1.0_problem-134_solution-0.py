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
    
	Do not include these tokens in the code: return True if txt . ends with
	'''
    
    # Convert txt to a list of characters
    txt_lst = list(txt)
    # Convert every element into an string
    txt_lst = [str(i) for i in txt_lst]

    if txt == "": return False

    if txt_lst[-1] in list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        if txt_lst[-2] == " ": return True
    else: return False
