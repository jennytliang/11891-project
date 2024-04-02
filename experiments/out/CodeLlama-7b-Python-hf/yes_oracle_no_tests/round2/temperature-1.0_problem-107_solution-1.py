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
    if n <= 0:
        return 0, 0

    n_str = str(n) + '0'
    n_len = len(n_str)
    even_count = odd_count = 0

    # odd _ cnt : count integer palindromes that fall within the range(1, n), inclusive
    odd_cnt = int(n_len / 2) + 1
    even_range = n_len // 2 + 1
    
    for num_odd in range(1, odd_cnt): # from 1 to 1digit # even_range
        if n_str[:num_odd] == n_str[-num_odd:]:
            odd_count += 1
            
    for num_even in range(1, even_range): # from 1 to 2digit # odd_cnt
        if n_str[:num_even] == n_str[-num_even:]:
            even_count += 1
    # print(f'odd = {odd_count} , even = {even_count}')
    
    # for number in range(n): # use a while loop if you like 
    return even_count, odd_count

    # count even integer palindromes that fall within the range(1, n), inclusive
    # odd_cnt = n//2 + 1
    # for odd_number in range(1, odd_cnt)

    # elif n_str[odd_cnt:odd_cnt+1] <= n:
    #     print('even palindome')
    
    # return (odd_count, odd_count)

def main(n):
    return even_odd_palindrome(n)

n = 5
result = main(n)
print(result)
    
if __name__ == "__main__":
    print(sum(main(100)))