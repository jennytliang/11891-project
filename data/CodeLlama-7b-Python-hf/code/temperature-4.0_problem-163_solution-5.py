def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # base case, b is less than the starting number
    if b < a: 
        return []
    if b%2 !=0:
        b = b+1
        a = b - 2

     # generate an integer from a to b (the range is given by the equation: 10x+y = 5 * (x+1))
    for numx in range(a/10, (b/10 + 1)):
         # then generate each y for the given x. y has to be odd.


         for y in range(1, 10):
        if (y + (10 * (numx - (a / 10))) )% 2 ==0:
            pass
        
         # if this number matches
        elif int((10 * (numx- (a/10)))+ y) > 0:
       
            x = (10 + (2* (numx - (a/10))))
         # return all of them, they're sorted by the sorting function
     return x

a, b = 9, 16

print('numbers within this range that are odd: ')
for number in range(5, 56, 2):
    print(number)
for i in generate_list(6,9)