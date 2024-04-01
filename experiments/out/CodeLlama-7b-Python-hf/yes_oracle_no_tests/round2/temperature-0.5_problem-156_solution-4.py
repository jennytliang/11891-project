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
    # TODO: write your solution here
    m = [" ", " m "]
    if number <= 0:
        print("Bad number")
    elif number >= 1000:
        print("Bad number")
    elif number >= 100:
        hundred = int((number-number%100)/100)
        hundred_name = "c" + m[hundred]
        if hundred_name == "c m":
            hundred_name = "d" + m[hundred]
        number = number - (hundred*100)
        hundred_name = hundred_name + int_to_mini_roman(number)
        return hundred_name
    elif number >= 10:
        ten = int((number-number%10)/10)
        ten_name = "x" + m[ten]
        if ten_name == "x m":
            ten_name = "l" + m[ten]
        number = number - (ten*10)
        ten_name = ten_name + int_to_mini_roman(number)
        return ten_name
    elif number >= 1:
        i = int(number)
        i_name = "i" + m[i]
        if i_name == "i m":
            i_name = "v" + m[i]
        return i_name

print(int_to_mini_roman(19))
print(int_to_mini_roman(152))
print(int_to_mini_roman(426))
