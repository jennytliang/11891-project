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
          
        return start + (end-start)/ 2           # Find the exact square root.
        # return start
        
    for i in range(1, iteractions):
         
        if (i%2) != 0 and (num==2): return True   # As 2 is a special case (most of times, as we want to check till 'N' is divisible).

        if(num**.5 % 1):                                # if no remainder after square root of 'N' (like 2,3 as a square root) then no use to divide and check, hence,  return's False.
            num_ = num                        # as we are taking square_root of number(haven't divided and got the quotient), hence we have to use same "value" again for next operations.
            # "num" is for the square root which is only to find out range for further iterations. 
            limit = num_ // 2
            start = 1
            end = limit
            ans = get_sqrt(num_, start, end)            # finding square root till nearest intiger before square-root.
         
            x = 5 if (ans - 5) > 4 else 2  # (if it's not getting square_root)  # it's for checking if square root is not getting exact then, by finding the nearest int and then start's next iterations' range with that value.   
        else:                                       # if square root got exact remainder(like 4,6,7...) then divide the number by it(to get exact "x") so that we will get proper iterations' range with it's divisor.           
            # x = int(num // int(num**.5))    # if so then to divide and get quotent by square root, (if we get the divisor) by dividing the original 'N' as we are not sure that we will have to divide with the nearest integer or the exact square_root of 'N'.                       # We are taking square root of number(got the quotient) as there will be times when number got exact sqrt(and it's a divisor) e.g., N = 49(2*root(49)) -> (5 & 49) but if no exact, then it won't be a divisor and hence we will have to check till it(e.g. 5).
               x = num // 2                               
               start = 6               # as from 5 we don;t check 7th time but, as from 5 to 2 there is range, so to start from next intiger from 5 to be used as range start 6 is used. 
               limit = start + x // 2

        end = start + int(x/2) # + x//2   # to define end 
      
        start = 6 if start != num else start+1
        # start=int(start)+1    # as it takes the value of "x" also in the range which is not necessary and as it is alredy checked above.
        for k in range(start, end + 1):                # Checking if number is a prime(not getting any divisor till it).
 
          
            if(num % k  == 0): 
             return False        # if any divisor found before the number ends it self then, the "k" is obviously not a prime as divisor exists and so the given "number" will be composite hence, return false            
       

 
 
 
 
 
 
    #print("after ", num//4, x, i, num) 


   
    return True                # as all the iterations and checks are passed then "n" is definitely a prime. 
