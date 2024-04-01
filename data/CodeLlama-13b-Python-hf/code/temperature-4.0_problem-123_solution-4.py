def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    if n<=0:
        raise ValueError("input is non-positive.")
    if n==1:
        return [1] # [1, 2] should not be considered as the odd numbers as well, since the 2 is not an odd number, but I guess it make sense here?
    odd_n = []
    while n>1:
        collatz_n = collatz(n)
        odd_n+=list(filter(lambda x : x%2!=0, collatz_n))
        n=1
        for i in range(len(collatz_n)-1, -1, -1):
            if n>collatz_n[i] and collatz_n.count(n)==1: # Ensure no repeated numbers and all the elements in the list is odd number only.
                n=collatz_n[i]
                n=1
                break
            else:
                break
        
        while n==1: # In case there's no repeated elements in the sequence.
            m=2
            while 2**m<n: # Ensure for the last odd number in the collatz sequence, which is 2**i in this example. The last element in this example would be 128.
                 if n<collatz_n[-m]: # Check for the last valid element that has an odd number before (2**i-1 in the sequence.)
                     n = collatz_n[-m]
                     break # There are no repeated numbers, and all the numbers on the left are even. All the rest is the same as above.
            if 2**m==n and n>=3:
                n+=1
                m=2+int(math.log2((int)(n))-0.5* (n%2==0)) # For the odd number, it is always the power of two, with either 2, 6 or 2+2(if 2).
                # E.g.: 21, 89, 132 ... are the numbers with odd sequence. 25, 53, 359, 1901, 4913 are numbers that cannot be on the odd number sequence.
            else: 
               m=2+int(math.log2((int)=(n)))
               n = 2**m
            while n==1:
                n+=1
            m=2
    return sorted(list(set(odd_n)) + 1)
            