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


# code to check provided number is prime or not in a more precise way

def check_prime_with_sqrt(num, iteractions=1):
    
    """ A number will be checked is prime(or not) till "iterations" time
        - if it will pass all iteration(by the way this doesn't guarantee but it will help in checking whether the no is indeed prime),
            then it return's true, otherwise "False."
        - if "iteraction=1"(bydefault), it checks 5 times by taking square root,
            then if it's not divisible by number between 3-5 then finally it return's true, that number is prime otherwise, it's composite."""



    def get_sqrt(num, start, end):
        if end - start < 2:
            if((num%start)):
               return end + 1
          
        return start + (end-start)/2