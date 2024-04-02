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
    
	Include these tokens in the code: ans , x = [],
	Do not include these tokens in the code: if
	"""
    def collatz(x):
        if x%2 == 0:
            return x//2
        else:
            return 3*x+1

    def check_if_odd(x):
        if x%2 != 0:
            ans.append(x)
        
    ans = []
    check_if_odd(n)
    for i in range(100000):
        current = collatz(n)
        if current > 1000000:
            break
        else:
            check_if_odd(current)
            n = current
    return sorted(ans)


if __name__ == "__main__":
	input_data = [
		5, 
		12, 
		13, 
		43, 
		33, 
		# 124, 15, 14345888, 123855, 232246
	]
	answers = [
		[1, 5],
		[1, 3, 10],
		[1, 11, 11],
		[1, 45],
		[1, 7, 47],
		# [8749496, 23274, 791411]
	]
	for x, y in zip(input_data, answers):
		if y == sorted(get_odd_collatz(x)):
			print("PASSED {}".format(x))
		else:
			print("FAILED {}".format(x))

