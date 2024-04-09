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
    m = [" ", " m "]
    dic = {1: "i", 4: "iv", 5: "v", 9: "ix", 10: "x", 40: "xl", 50: "l", 90: "xc", 100: "c", 400: "cd", 500: "d",
           900: "cm", 1000: "m"}
    result = ""
    for key in sorted(dic.keys())[::-1]:
        while number >= key:
            result += dic[key]
            number -= key
    return result.lower()


print(int_to_mini_roman(19))
print(int_to_mini_roman(152))
print(int_to_mini_roman(426))