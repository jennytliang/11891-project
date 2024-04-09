def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    
	Include these tokens in the code: odd _ cnt ,
	Do not include these tokens in the code: #
	"""
    # Initialization
    odd_cnt = 0
    even_cnt = 0
    # End of Initialization

    for i in range(1, n + 1):
        if i % 2 == 0:
            # Loop through all even numbers
            # and check if they are palindrome
            temp = i
            rev = 0
            while temp != 0:
                rev = rev * 10 + temp % 10
                temp = temp // 10
            if i == rev:
                even_cnt += 1
            else:
                odd_cnt += 1
        else:
            # Loop through all odd numbers
            # and check if they are palindrome
            temp = i
            rev = 0
            while temp != 0:
                rev = rev * 10 + temp % 10
                temp = temp // 10
            if i == rev:
                even_cnt += 1
            else:
                odd_cnt += 1

    return (even_cnt, odd_cnt)


def main():
    print('Byron Kim')
    print('Problem 1')
    print('Odd and Even Palindrome')
    print('Sample Input:')
    print('3')
    print('Sample Output:')
    print('(1, 2)')
    print('-------------------------------------')
    print('Input:')
    print('12')
    print('Output:')
    print('(4, 6)')
    print('-------------------------------------')
    print('Input:')
    print('100')
    print('Output:')
    print('(25, 75)')
    print('-------------------------------------')
    print('Input:')
    print('200')
    print('Output:')
    print('(50, 150)')
    print('-------------------------------------')
    print('Input:')
    print('1000')
    print('Output:')
    print('(500, 500)')
    print('-------------------------------------')

    n