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
    
	Include these tokens in the code: ans , x = [], n
	"""
    # Your code here
    x = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        x.append(n)
    ans = []
    for i in range(0, len(x)):
        if i % 2 == 1:
            ans.append(x[i])
    return sorted(ans)


# simple test
if __name__ == '__main__':
    input = 5
    output = [1, 5]
    result = get_odd_collatz(input)
    if output == result:
        print('Test passed!')
    else:
        print('Test failed!')
        print('Input: ', input)
        print('Output: ', output)
        print('Result: ', result)
