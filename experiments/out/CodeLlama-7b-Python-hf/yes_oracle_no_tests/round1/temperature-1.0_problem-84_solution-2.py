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
    
	Include these tokens in the code: s = sum ( map ( lambda x : int
	"""
    pass


# ==================================================================================================
if __name__ == "__main__":
    # print(f"solve(45) = {solve(45)}") # 45 = 4 + 5 = 9
    assert solve(1000) == "1", "Should be a string with a binary number 1"
    assert solve(150) == "110", "Should be a string with a binary number 110"
    assert solve(147) == "1100", "Should be a string with a binary number 1100"
    print('"Okay"')