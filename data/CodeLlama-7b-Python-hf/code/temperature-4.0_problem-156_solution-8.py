def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

    string = ''
    for name in 'm', 'c', 'x':
        if number >= len(name):
            number, index = len(name), string.index(name)
            string = ''
            string += string[: index] + name
        else:
            pass
    for digit, name, place, small_roman in (
        ((number - (len('c') + len('i') ) ), 'c', 'vii', 'ix'),
        (len(string) == len('x') + len('i'), 'm', 'iii', 'iv')  ):

        if (not digit): # and (small_roman != string) :  # only one of those at end of num, or just m or nothing in num (case 'xix' )
            # if (not digit) and digit == int(str(number)[0]):  # 'c'
                string = string + ('i')
                string = string + place
            elif digit == int(str(number)[0]): #case 'cc'
                if string:  string = string [:-(int(len(place))) ]   # delete 'llxxx' at end of num
                else : string = place
            elif digit == len(small_roman):  # only 1 small roman letter in the end of a three-letters, else add m
                if string[-1] == 'mm' :string = string[:(int(string[:len('lm')]))]
                string += small_roman[:(int(1))] # if 0, so just 'i'
    if not string[-2:-1]=='i' :
     string = string[:len(string) - 2] # delete second i
    print (string)
    return str.lower(
               string
            ) 
    return int_to_roman(int (number)) [int((len(string) / 2,)) : int(-1,)],string