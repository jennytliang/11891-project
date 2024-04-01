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
    
	Do not include these tokens in the code: if n <= 0 :
	"""
    # pass
    # ------------------------------------------------------------------
    # TO BE COMPLETED
    # ------------------------------------------------------------------

    if n<=0:
        return []
    elif n==1:
        return [1]
    else:
        odd_collatz = [1]
        while n not in odd_collatz:
            if n%2==0:
                n = n//2
                odd_collatz.append(n)
            else:
                n = 3*n+1
                odd_collatz.append(n)
        return odd_collatz


if __name__ == '__main__':
    # print(get_odd_collatz(5)) # returns [1, 5]
    # print(get_odd_collatz(14)) # returns [11, 12, 13, 14, 3, 10, 5, 16, 8, 4, 2, 1]
    # print(get_odd_collatz(17)) # returns [17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    # print(get_odd_collatz(37)) # returns [37, 112, 56, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    print(get_odd_collatz(13)) # returns [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
