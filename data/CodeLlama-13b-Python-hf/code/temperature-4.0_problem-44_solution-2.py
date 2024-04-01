def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if (not isinstance(x, (int, list)) or not (base < 10)):
        raise TypeError('The function change_base() just accepts integer input \
                        with base less thatn than 10. ')
    digits = [int(digit) for digit in list(str(x))]
    return_string = ''
    is_base2 = True
    if(x == 0):
        # For the purpose of consistency of returning string, I add a space for the 0.
        return '0 '
        return False

    while(x >= base and is_base2 is True):  # for base=2 we check whether x>=2 or x<2 and return a string of 1's or 0s accordingly
        
        if isinstance(x - int(str(base)[digits[0]])*base**digits[1], int) is False:
            return False

        remainder = x % base
        
        return_string = str(remainder).replace('.0', '') + return_string
        x = int(x / base )
        digits = ([0, 1] if (remainder != 0 and digits[0] == 1) else [
                0] + digits[:]) if (is_base2 ) else sorted(set(list([0, 1]) + [n for n in ([0, i] if int(digit) == 1 else [0] if n < i and i != 0 else
                                                                [i] for i in range(1, base) if digit > int(digit) or int(digit) < i] for digit in digits[:]))) if (x != 0 ) else [int(digit) for digit in str(x/base)]
        if base != 2:
            is_base2 == False

    return_string += ('' + str(x)) + return_string 
    return return_string

def change_base2(b, n):
    string_list = [i for i in change_base(b,10)]
    if (n-2) >= 0:
        return "1"+" "+"0"*n+"." + "".join([(string_list.pop() - 1).__str__() for k in range(0,int((n+2)/(len(string_list)+1))) ])