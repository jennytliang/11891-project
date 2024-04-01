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
    print(prime)      