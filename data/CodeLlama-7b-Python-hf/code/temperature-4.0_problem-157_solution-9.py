def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    if a> b and a>c:
        if (a<b+c) and (a*a) == (b*b+c*c):
            return True
        else:
            return a<b+c 
    
def pythagornas(a, b, c, d, n=None):
    '''
    Find if all the elements are in the right triangle. The function checks the condition a, b > 0 . The function can be used in any dimension. It can check 4 sides in a 2d triangle or 5 sides in a 3d triangle etc .
    Note: All the inputs must be of same dimensions
        
        Example: Input : pythagornas([1,2],[1,3], [4,3],[2,1]) OUTPUT: (0,1) , a1, b1 are indexs or the numbers.
    '''
    n=None
