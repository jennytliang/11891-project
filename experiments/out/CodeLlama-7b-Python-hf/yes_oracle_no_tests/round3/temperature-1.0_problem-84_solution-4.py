def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    
	Include these tokens in the code: s =
	Do not include these tokens in the code: # write your code here
	"""
    # 1. 1000 = 1111101000
    # 2. 1111101000 = 1111101000
    # 3. 1111101000 = 1000000111 + 101000
    # 4. 1000000111 + 101000 = 1111101000
    # 5. 1111101000 = 1111101000
    # 6. 1111101000 = 1000000111 + 101000
    # 7. 1000000111 + 101000 = 1111101000
    # 8. 1111101000 = 1111101000
    # 9. 1111101000 = 1000000111 + 101000
    # 10. 1000000111 + 101000 = 1111101000
    # 11. 1111101000 = 1111101000
    # 12. 1111101000 = 1000000111 + 101000
    # 13. 1000000111 + 101000 = 1111101000
    # 14. 1111101000 = 1111101000
    # 15. 1111101000 = 1000000111 + 