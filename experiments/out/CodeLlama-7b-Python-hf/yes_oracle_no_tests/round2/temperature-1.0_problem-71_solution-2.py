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
    
	Include these tokens in the code: + b
	'''


   def triangle_area(a,b,c):
    p2=b**2+c**2
   if a**2+b**2>=c**2:
    return math.sqrt(p2-2*a*b*math.sqrt(p2))



def checkio(data):
    # Your code here
    a=data[0]
    b=data[1]
    c=data[2]

    if a+b>=c and b+c>=a and a+c>=b:
        v=triangle_area(a,b,c)
        return round(v,2)
    else:
        return -1


print(checkio([2, 2, 2]))
print(checkio([9, 10, 17]))
