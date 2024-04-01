def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_divisor = 1
    largest = 2    
    # loop through all the integers from 2, till half of n, step 1
        # if that int (prime) divdes n, then n = the new number (d)
    for prime in range(2, (n // 2)+1, 10): 
        k = 0 # to make sure that every number does have a multiple and not because we did not check
        i = prime # starts with the first prime, since we do not need to do anything with it when we are on the first loop
        while  k==0 or n % prime !=0 or i==1 or n % i ==1:      # if we have found the correct prime, the k will be set as 2 if that happens
            # and then we will be outside the i loop and increase the counter so that 29 is the correct answer
            i -= 1                    # we decrease to a number before i to make sure we can check all numbers before that one        
            k +=1
        else:  # if we are inside the loop and k =2 and we do have found the prime we will break from the k loop     
             # and then set the value of number as the number we found instead of the number which was left after dividing
            k+=1
            k=1
    print(largest) # to make sure that it will also work with other numbers, you can uncomend this
#    elif n == prime and n != 1:
        # if it is not true for the largest we will set it now
#    elif n !=1:
        # also in this case we want to add a if statement when n is a prime number itself.
    return largest


def is_prime(i):
    # we will add later the statement to make sure that n isnt a prime
    
    k = 0
    for prime in range(2, (int(n // 2) +0), 5):    
        # firstly we will take all the primnes starting from 2 to 10 for instance
        l = 0 # also a counter, since the number does not always devide the current prime so that we make sure that that happens before we can break
        # but also in the while loop
    # now for every prime number until we divide it, we divide it by that number and check
    # if the answer is zero, we can stop the current loop because n has devided prime
    # and we will have the result
        if n % prime == 0 or i < prime :      # if we found a prime devidor and the prime number we are on does not divide n itself we are done here
            break
        else:   # if the prime number divided but did not give zero, we want that counter to be increased everytime
        # so it does work for every prime we will be checking
            # also we will save the primedivisiors in list so that we could check the list and if they do divide the
    print(largest1) # i added this just in case i could check which prime number does devide n exactly
# for checking the program, use a print statement for the program, to be able to check it, the print statement might be
# helpful, but i can do the whole program without using one
    