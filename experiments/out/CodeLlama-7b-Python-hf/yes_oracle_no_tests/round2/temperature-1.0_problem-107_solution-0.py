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
    ## EDGE CASE 1 ##
    if n < 1 : return (n, -1)
    
    ## INITIALIZE VARIABLES ##
    even_cnt = 0
    odd_cnt = 0
    x_range = set(range(1, n + 1))
    all_nums = set()
    
    ## BUILD ALL INTEGERS FROM 1 SMALLER THAN `N` ##
    for i in reversed(range(n + 1)) : # RANGE OMNES 4 WAITS MILTIPLICATO DE LOS 5
        if i not in all_nums:
            for num in range(10):
                y = (num * i)
                if y in x_range and y not in all_nums:
                    all_nums.add(y)
    
    ## COUNT THE PALINDROMES IN `A` ##
    for x in all_nums:
        str_x = str(x)
        
        ln = len(str_x)
        div = ln // 2
        
        if ln %2 == 1 :
            odd_cnt += 1
        else :
            odd_cnt += 1
            div -= 1
            
        if str_x[:div] == str_x[-div:]:
            even_cnt += 1
        else:
            even_cnt += 0
    
    return (even_cnt, odd_cnt)
