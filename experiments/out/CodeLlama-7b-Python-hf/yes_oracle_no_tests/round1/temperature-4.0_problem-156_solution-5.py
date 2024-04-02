def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: m = [" ", " m "] c
	"""
    m = [" ", " m "]
    c = ["i", "x", "c"]
    d = ["", "d", "cd"]
    o = ["", "o", "c"]
    t = ["", "t", "ct"]
    h = ["", "h", "c"]
    
    num_str = str(number)
    
    num_list = [int(x) for x in num_str]
    
    num_list.reverse()
    
    result = ""
    
    for i in num_list:
        if i == 1:
            result = result + c[num_list.index(i)]
        elif i == 2:
            result = result + c[num_list.index(i)] + c[num_list.index(i)]
        elif i == 3:
            result = result + c[num_list.index(i)] + c[num_list.index(i)] + c[num_list.index(i)]
        elif i == 4:
            result = result + c[num_list.index(i)-1] + c[num_list.index(i)]
        elif i == 5:
            result = result + c[num_list.index(i)-1]
        elif i == 6:
            result = result + c[num_list.index(i)-1] + c[num_list.index(i)] + c[num_list.index(i)]
        elif i == 7:
            result = result + c[num_list.index(i)-1] + c[num_list.index(i)]
        elif i == 8:
            result = result + c[num_list.index(i)-1] + c[num_list.index(i)] + c[num_list.index(i)] + c[num_list.index(i)]
        elif i == 9:
            result = result + c[num_list.index(i)-1] + c[num_list.index(i)] + c[num_list.index(i)]
        elif i == 0:
           