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
    # write your answer between #start and #end
    #start
    ans = []
    x = []
    for a in range(1, n + 1):
        if a % 2 != 0:
            x.append(a)
    for b in x:
        while b != 1:
            if b % 2 == 0:
                b = b / 2
            else:
                b = 3 * b + 1
            if b not in x:
                x.append(b)
    return sorted(x)
    #end


print('Test 1:')
print('Expected:')
print([1, 5])
print('Actual:')
print(get_odd_collatz(5))

print('Test 2:')
print('Expected:')
print([1, 7])
print('Actual:')
print(get_odd_collatz(7))

print('Test 3:')
print('Expected:')
print([1, 9, 15, 21, 35, 45, 63, 75, 97, 127])
print('Actual:')
print(get_odd_collatz(100))

print('Test 4:')
print('Expected:')
print([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93,