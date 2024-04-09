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
    
	Include these tokens in the code: odd _ cnt , even _ cnt =
	"""
    # 1-100
    # 101-200
    # 201-300
    # 301-400
    # 401-500
    # 501-600
    # 601-700
    # 701-800
    # 801-900
    # 901-1000

    # odd _ cnt = 1+2+3+...+99+100
    # even _ cnt = 201+202+203+...+300+301
    # odd _ cnt = 401+402+403+...+400+401
    # even _ cnt = 601+602+603+...+600+601
    # odd _ cnt = 801+802+803+...+800+801
    # even _ cnt = 1001+1002+1003+...+1000+1001

    # odd _ cnt = 1+3+5+...+99+101
    # even _ cnt = 202+204+206+...+200+202
    # odd _ cnt = 403+405+407+...+401+403
    # even _ cnt = 604+606+608+...+602+604
    # odd _ cnt = 805+807+809+...+803+805
    # even _ cnt = 1006+1008+1010+...+1004+1006

    # odd _ cnt = 1+2+3+...+99+100
    # even _ cnt = 2