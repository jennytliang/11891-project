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
    numToRoman = {0:'', 1:'i', 2:'ii', 3:'iii', 4:'iv', 5:'v', 6:'vi', 7:'vii', 8:'viii', 9:'ix'}
    # numToRoman = {0:'', 1:'i', 2:'ii', 3:'iii', 4:'iv', 5:'v', 6:'vi', 7:'vii', 8:'viii', 9:'ix'}
