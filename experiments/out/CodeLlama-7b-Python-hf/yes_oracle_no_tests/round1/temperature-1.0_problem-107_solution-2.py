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
    # odd palindrome count
    odd_cnt = 0
    # even palindrome count
    even_cnt = 0

    for i in range(1, n+1):
        if i < 10:
            # if a single digit number
            # add it to the count
            if i % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
        else:
            # get the last digit
            last_digit = i % 10
            # get the first digit
            first_digit = i // 10

            # if last and first digit are equal
            if last_digit == first_digit:
                # if number of digits is even
                if len(str(i)) % 2 == 0:
                    even_cnt += 1
                # if number of digits is odd
                else:
                    odd_cnt += 1
            # if last and first digit are not equal
            else:
                # get the middle digit
                middle_digit = i // 10**(len(str(i)) // 2)
                # if middle digit is equal to last digit
                if middle_digit == last_digit:
                    # if number of digits is even
                    if len(str(i)) % 2 == 0:
                        even_cnt += 1
                    # if number of digits is odd
                    else:
                        odd_cnt += 1

    return (even_cnt, odd_cnt)
