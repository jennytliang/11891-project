def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    if not any([type(a) == int, type(b) == int]) or abs(min(a,b)) < 10:
        raise Exception("Input arguments have to be integers 10 and above")   
    x = str(a)[-1] + str(b)[-1]
    if x.isdigit() or x[0] == "-":
        print(int(x[0]))  
    elif abs(x[-1])>10:
        raise TypeError("number too large/small")
    return abs(int(x.replace(-"",x)))
      
    
    


# def multiply(a, b):             