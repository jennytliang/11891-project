def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: m = [" ", " m "]
	"""
    m = ["", " m ", "mm ", " mmm"]
    
    num = list(str(int(bin(number)[2::])[2::]))
    num = list(reversed(num))

    r = {"0111": m(4),
         "0011": m(3),
         "0001": m(2),
         "0000": m(1)} + {
         "1" + str(i): m(i) for i in (1, 2, 3, 4)}

    if int(number) == 0:
        return " "

    return "".join([r[num[i]*str(int(i))] for i in range(len(num))])\
           .replace("mmmm", "d")\
           .replace("vv", "w")\
           .replace("iiii", "iv")
