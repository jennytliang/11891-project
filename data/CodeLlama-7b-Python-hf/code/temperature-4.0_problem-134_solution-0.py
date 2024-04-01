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
    '''
    # Create function to check if last char is last word, char:
    def isLetterLastWord(c): 
        return any(c.count(x) for x in c.strip())
    
    # Create new list to add elements to, and check if each letter is the last in a word and add this to the list. 
    list_of_letters_in_str = txt.split(" ")
    checkLetter =[]
    
    #  Create a function for each letter in the list to check if it
    
    for c in list_of_letters:
        if c.endswith(c) == True:
