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
    if n%2 == 0: #if its even
        n//=2 #divide n/2
        return [n] + odd_collatz #return that list plus what this recursive function returnes in the same position (1)
    elif n >= 1: #if it is odd, it must have passed the test above already
                 #so the next number is 3n + 1 and we add the result from that recursively to list
        a = 3 * (int(n))+ 1 #calculate the result for recursive
        return [n]+get_odd_collatz(int(a)) # return odd numnber and recursive results concatenated to it as a list
    else: return #if it cannot divide 2 and not an even number it cant be odd
        
        

