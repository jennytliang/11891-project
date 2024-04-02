from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    dictionary={"zero":0,
                "one":1,
                "two":2,
                "three":3,
                "four":4,
                "five":5,
                "six":6,
                "seven":7,
                "eight":8,
                "nine":9}
    lst=numbers.split(" ")
    lst[-1]=lst[-1].strip(",")
    lst2=[]
    lst2[:0]=lst
    for i in range(len(lst2)):
        if lst2[i] in dictionary:
            lst2[i]=dictionary[lst2[i]]
        else:
            lst2[i]=lst2[i].strip(",")
    lst3=[]
    for i in range(len(lst)):
        lst3.append(lst2[lst2.index(min(lst2))])
        lst2.pop(lst2.index(min(lst2)))
    lst3[-1]=lst3[-1].strip(" ")
    return " ".join(str(j) for j in lst3) 



def sort_digits(digits: str) -> str:
    """Input is a space-delimited string of only unique digits,
so 'zero' through 'nine'.  Return the string of digits sorted numerically from smallest to largest
>>> sort_digits('five six seven')
'five six seven'

Include these tokens in the code: int str = ''
"""
    lst=digits.split(" ")
    lst[-1]=lst[-1].strip(",")
    lst2=[]
    lst2[:0]=lst
    for i in range(len(lst2)):
        if lst2[i] in dictionary:
            lst2[i]=dictionary[lst2[i]]
    lst3=[]
    for i in range(len(lst)):
        lst3.append(lst2[lst2.index(min(lst2))])
        lst2.pop(lst2.index(min(lst2)))
    lst3[-1]=lst3[-1].strip(" ")
    return " ".join(str(j