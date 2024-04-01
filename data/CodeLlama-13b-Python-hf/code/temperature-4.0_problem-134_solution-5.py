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
    a = list(
        map((lambda char:  char == char.lower() and char != ' '), list(txt[-1:]))
    )
    # return a[0] if a else False

""" """

def validate_email_address2(email):
    # print(f'Inside val func: {email}, {type(str_input)} ')
    if (email == None or not email or len(email) < 2):
        return {'error':"Invalid email address, please enter an email address"}

    result = False
    is_valid = "Valid email address"
    is_invalid = "Invalid email address format"
    user, domain = email.split('@')

    if(user.isalnum() and
            "." in domain and
            max(domain.split(".")) <= 3 and
            email[-3] != '.'
    ) :
        result = True
    return
""" def is_email_valid(email, domain):

        if (len(email)>0 and '@' in email and email.count(".") == 1 and domain.isalnum()):  
                print('is Valid Email')    
        if (len(name)>3):  
                print('Name is too Short, should be 3 or more characters.')



        if(not ('@') in email):
           return 'Email not valid, it needs @'

        #domain = get_domain(email)
