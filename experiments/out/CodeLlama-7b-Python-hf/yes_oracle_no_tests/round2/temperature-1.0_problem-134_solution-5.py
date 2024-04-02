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
    
	Include these tokens in the code: if
	Do not include these tokens in the code: result =
	'''
     #split the txt txt to words and then check if the last word has alphabets
    lst=txt.split(" ")
    x=lst[-1]
    return chk_final_char(x)


def chk_final_char(char):
    '''
    
    Note: "word" is a group of characters separated by space.
    
	'''
     #check if the last character of a word is a alphebet
    #split the txt txt to words and then check if the last word has alphabets
    if any(l.isalpha() for l in char):
         return True
    else:
        return False
print(check_if_last_char_is_a_letter("apple pie"))
print(check_if_last_char_is_a_letter("apple pi e"))
print(check_if_last_char_is_a_letter("apple pi e "))
print(check_if_last_char_is_a_letter(""))

#Other solutions
def check_if_last_char_is_a_letter_v2(txt):
    lst=txt.split(' ')
    x=lst[-1]
    return any(x[-1].isalpha())
check_if_last_char_is_a_letter_v2("apple pie")  

def check_if_last_char_is_a_letter_v3(txt):
    lst=txt.split(' ')
    x=lst[-1]
    return x.isalnum()
check_if_last_char_is_a_letter_v3("apple pie")  

def check_if_last_char_of_the_word_is_a_letter(txt,n):
    lst=txt.split(' ')
    x=lst[n]
    return x[-1].isalpha()
check_if_last_char_of_the_word_is_a_letter("apple pie",0)
