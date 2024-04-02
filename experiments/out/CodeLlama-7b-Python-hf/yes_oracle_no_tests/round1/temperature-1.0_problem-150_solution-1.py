def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: if n > 1 :
	"""

    if(a < 1):
        return "Enter a number larger than one"
    i = 2
    while(i <= a):
        if(a % i == 0):
            return y
        i += 1
    return x


# IGNORE CODE BELOW, IT'S NOT MEANT FOR LOOKING (yet!)
if __name__ == '__main__':
    a = input("Input a value for a(number): ")
    x = input("Input a value for x(answer): ")
    y = input("Input a value for y(answer): ")
    result = x_or_y(int(a), int(x), int(y))
    print(result)
