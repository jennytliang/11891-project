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
    
    num = int(number)
    if num==0:
        return ''
    else: 
        if num<4:
            return numToRoman[num%10]
        elif num<400:
            if num<100:
                if int(num/10)<4:
                    return num % 10 * numToRoman[int(num/10)%10]
                elif int(num/10)==4:
                    return numToRoman[int(num/10)%10] * 'iv'
                else:
                    return numToRoman[int(num/10)%10] * numToRoman[int(num/10)]
            elif num<400:
                if int(num/100)==5:
                    return 'v' + numToRoman[int(num%10)]
                elif int(num/100)==9:
                    return 'x' + numToRoman[int(num%10)]
                else:
                    return numToRoman[int(num/100)] + 'c' + numToRoman[int(num%10)]
        else:
            if num<500:
                return 'd' + numToRoman[int(num%100)]
            elif num<900:
                return numToRoman[int(num/100)] + 'c' + numToRoman[int(num%100)]
            elif num==1000:
                return 'm' + numToRoman[int(num/100)]
    # print(numToRoman)

