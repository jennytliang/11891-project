def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    # FIXME: add error checking the inputs
    return 0.5 * a * h 


def get_hypothenuse_right_angle(c, alpha):
    """
    Given a length from the right angel and the angle, return the length of hypotenuse
    https://kinsta.com/blog/mathematics-of-right-angled-triangle/
    https://science.evgenii.org/topic-find-right-angled-triangle-side/
    https://ediscretestudents.files.wordpress.com/2014/03/triangle_2.gif

    a^2 + (c/sin_x)^2 = b
    45.77

    17.31

    c = h * sin(A)  
    h = 45.6768024652716
    h = (c / sin(60 deg)) = sin_x / sin(60 deg)


    8.5
    6.306711263146854 = hypotenuse / sin(52.32) 
    72.68422814696167

    72.55013767972889



    sin(52.32) =

    """
    A = (90 - alpha) / 90
    sin_x = A
    a = c / sin_x
    # return b, h
    # b = 61.65222796991921 / 2
    # h = 16.026666319798042
    # b = 72.55156085928588
    # hypothenuse / sinx = sin(angle)
    # hyp = 8.5 #
    hyp = c * (cos(alpha)) #
    # hyp = 9.005036132966927 #
    h = hyp / sin_x
