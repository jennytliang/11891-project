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
    # YOUR CODE HERE
    m = [" ", " m "]
    number = str(number)
    roman = []
    for i in range(len(number)):
        if number[i] == "1":
            roman.append("i")
        elif number[i] == "2":
            roman.append("i")
            roman.append("i")
        elif number[i] == "3":
            roman.append("i")
            roman.append("i")
            roman.append("i")
        elif number[i] == "4":
            roman.append("i")
            roman.append("v")
        elif number[i] == "5":
            roman.append("v")
        elif number[i] == "6":
            roman.append("v")
            roman.append("i")
        elif number[i] == "7":
            roman.append("i")
            roman.append("i")
            roman.append("i")
            roman.append("i")
        elif number[i] == "8":
            roman.append("i")
            roman.append("i")
            roman.append("i")
            roman.append("i")
            roman.append("i")
        elif number[i] == "9":
            roman.append("i")
            roman.append("v")
            roman.append("i")
    roman = "".join(roman)
    for i in range(len(roman)):
        if roman[i] == "v":
            if roman[i+1] == "i":
                roman = roman.replace("v", "u")
    for i in range(len(roman)):
        if roman[i] == "x":
            if roman[i+1] == "i":
                roman = roman.replace("x", "y")
    for i in range(len(roman)):
        if roman[i] == "d":
            if roman[i+1] == "i":
                roman = roman.replace("d", "w")
    for i in range(len(roman)):
        if roman[