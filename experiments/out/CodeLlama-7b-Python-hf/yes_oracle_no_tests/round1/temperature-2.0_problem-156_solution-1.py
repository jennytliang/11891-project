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
    # m = ["I", "V", "X", "L", "C", "D", "M"]
    m = [" ", " m "]
    result = ""
    i = 0
    while number > 0:
        if number % 10 == 9:
            result = result + m[i] + m[i+1]
            number = number - 10
        elif number % 10 == 4:
            result = result + m[i] + m[i+2]
            number = number - 5
        elif number % 10 == 5:
            result = result + m[i] + m[i+1] + m[i+2]
            number = number - 5
        elif number % 10 == 6:
            result = result + m[i] + m[i+2] + m[i+1]
            number = number - 6
        elif number % 10 == 8:
            result = result + m[i] + m[i+2]
            number = number - 10
        else:
            result = result + m[i] + m[i+2] + m[i+1] + m[i+2]
            number = number - 9
        i += 2
    return result

print(int_to_mini_roman(19))
print(int_to_mini_roman(152))
print(int_to_mini_roman(426))