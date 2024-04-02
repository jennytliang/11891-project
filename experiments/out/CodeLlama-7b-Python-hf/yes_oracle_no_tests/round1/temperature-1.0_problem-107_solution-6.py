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
	"""
    odd_cnt = 0
    even_cnt = 0
    
    for i in range(1, n+1):
        while i > 0:
            curr_n = i%10
            i = i//10
            
            check_num = 0
            while check_num <= curr_n:
                check_num += check_num*10 + curr_n
                odd_cnt += 1
            if check_num == 0:
                even_cnt += 1
    return (odd_cnt, even_cnt)
