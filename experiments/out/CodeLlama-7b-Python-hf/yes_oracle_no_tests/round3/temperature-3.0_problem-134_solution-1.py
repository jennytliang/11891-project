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
    
    if len(txt) == 0:
      return False
    elif txt[-1].isalpha():
      return False
    else:
      return True

#print(check_if_last_char_is_a_letter("apple pie")) #➞ False
#print(check_if_last_char_is_a_letter("apple pi e")) #➞ True
#print(check_if_last_char_is_a_letter("apple pi e ")) #➞ False
#print(check_if_last_char_is_a_letter("")) #➞ False 


def is_palindrome(txt):
    '''
    Write a function that checks if a given string is a
    palindrome.
    
    Notes:
    - A palindrome is a word that is spelled the same backward and forward.
    - For this problem, you can consider punctuation and spaces to be part of a word.
    - You can also consider an empty string to be a palindrome.
    
    Examples:
    is_palindrome("radar") ➞ True
    is_palindrome("radar?") ➞ True
    is_palindrome("radar?!") ➞ True
    is_palindrome("radars") ➞ False
    is_palindrome("radars!") ➞ False
    
    Notes:
    - You can assume the input is a string.
    - You can convert the string into lower case if it helps you with your solution.
    - You can also remove punctuation and spaces if it helps you with your solution.
    - If you do remove spaces, the first and last indices of the string should still be considered to be part of the string.
    - You might need to use slicing.
    - You might need to use the isalpha() method.
    '''
    
    if len(txt) == 0:
      return True
    elif txt[0].isalpha() == False:
      return is_palindrome(txt[1:])
    elif txt[-1