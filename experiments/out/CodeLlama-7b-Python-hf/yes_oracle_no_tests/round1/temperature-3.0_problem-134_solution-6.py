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


def check_if_has_more_vowels_than_consonants(txt):
    '''
    Create a function that returns True if a given string has more vowels 
    than consonants, and False otherwise.
    
    Examples:
    check_if_has_more_vowels_than_consonants("hello") ➞ True
    check_if_has_more_vowels_than_consonants("helloworld") ➞ False
    check_if_has_more_vowels_than_consonants("codewars") ➞ True
    
    Notes:
    Vowels are: a, e, i, o, u.
    Consonants are: all the rest excluding vowels.
    '''
    #code goes here
    vowels = 0
    consonants = 0
    for i in txt:
        if i.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    return vowels > consonants

#check_if_has_more_vowels_than_consonants("hello") #, True)
#check_if_has_more_vowels_than_consonants("helloworld") #, False)
#check_if_has_more_vowels_than_consonants("codewars") #, True)


def check_if_last_4_digits_are_