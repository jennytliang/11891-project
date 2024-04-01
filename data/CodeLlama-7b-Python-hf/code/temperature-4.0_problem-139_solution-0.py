def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """

    # write your own conversion and tests
    specialFact = 1
    if n == 0: 
        print("Please, type a positive integer")

        i = int(input())
        specialFact = i

    elif n > 0:
        for c in range (1, n): 
            

            if c <= len (str(int(n/c))) or c == 0:
                specialFact = specialFact*i
                print(specialFact)    

        

    
    return specialFact    