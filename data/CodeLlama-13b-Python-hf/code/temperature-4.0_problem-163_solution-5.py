def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    evens= [2,4,6,8,10,1,3,5,7,9]
    lst=[]
    if (a==11 or a==12):
        a=13
    for i in range(2, a):
        if i%2!=0:
            lst.append(i)
    return [x for x in evens if a<= x <=b]          
    # generate the lst of odd numbers first then loop thorugh the odd numbers
    # and print if they are even
print(generate_integers(34,42))