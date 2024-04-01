def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    z=1
    if(n<2):                                     # If the input given is not 
        z=0                                      # positive prime number then it will return null i.e, 0.

    else:                                        # The loop will iterate and check for the number is prime or composite
        for i in range (2,int(n/2+1),1):                 # Checking the number up to n(as we want output from 2 till the given number not including it). We also divided the number in two as we know that all prime numbers are either even or odd.
            # if(i ** 2==1): 
            #     continue
            if(n % i) == 0:                      # If after dividing n (number) by any number i and remainder of division by i(i.e., R) comes zero then, the given number is "not" prime and loop breaks
                z=0
                break
        if(z==0):
            z+=1
            return y   # If loop breaks then returns y value, i.e, if it is not "prime" number. 
        else:
            return x      # If loop does not break then only it returns X, i.e., If it's a prime number.   

    return z