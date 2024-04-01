def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    if a + b <= c or b + c <= c or a + c <= b:
        return -1
    else:  
    # Calculate the Area using Heron Formula S=(a+b)c/2 where c = side length 
    # given by the formula. The value obtained should be stored and passed to the round fn
        a = int(input("Enter first value of side of triangle: ")) # inputting first number in the Triangle
        c = 15                                       # inputting a third number to give us a 'Triangle' ie 5,12...etc
        # calculating the area using formula
        side_area = (a + c) * c 
        #calling the 'roundfn'
        print("the Area for a triangle sided with the number",a, "is:", area())

def area():
    # the function returns the area using the formula given
    return(round(side_area /2, 2))
# the code calling the function to return the value 'area' to print statement: