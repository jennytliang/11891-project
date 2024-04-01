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
    # The squared equation of the circle is:
    # x^2 + y^2 = c
    def get_right_angled_triangle(x, y, x_sqr, c):
        return False if x == y  or x+y > c else True 
    def get_lengths_sum(x, y):
        return float((x_squared+y_squared))
        
    

    return "False, not a triangle" if get_lengths_sum(a,b)<c or c<get_lengths_sum(a,b) else "True, it is triangle and it right angled "