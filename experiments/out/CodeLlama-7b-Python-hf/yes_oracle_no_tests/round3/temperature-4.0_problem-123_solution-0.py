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
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n % 2 == 0:
        x = n // 2
    else:
        x = 3 * n + 1
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
    if n not in ans:
        ans.append(n)
    return ans


def main():
    print(f"get_odd_collatz(5): {get_odd_collatz(5)}")
    print(f"get_odd_collatz(1): {get_odd_collatz(1)}")
    print(f"get_odd_collatz(2): {get_odd_collatz(2)}")
    print(f"get_odd_collatz(3): {get_odd_collatz(3)}")
    print(f"get_odd_collatz(4): {get_odd_collatz(4)}")
    print(f"get_odd_collatz(6): {get_odd_collatz(6)}")
    print(f"get_odd_collatz(7): {get_odd_collatz(7)}")
    print(f"get_odd_collatz(8): {get_odd_collatz(8)}")
    print(f"get_odd_collatz(9): {get_odd_collatz(9)}")
    print(f"get_odd_collatz(10): {get_odd_collatz(10)}")


if __name__ == "__main__":
    main()
