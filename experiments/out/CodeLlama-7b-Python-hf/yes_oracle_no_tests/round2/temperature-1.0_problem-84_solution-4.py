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

    def sum_binary(number):
        binary = binarify(number)
        return sum([int(item) for item in binary])
        # return sum([1 for item in binary])

    def binarify(number):
        return bin(number)[2:]
    
    def make_all_zeroes(binary_number):
        length = len(binary_number)
        return '0'*(length)
        
    total_result = sum_binary(N)

    if total_result == 0:
        return binarify(0)
    
    return make_all_zeroes(str(int(total_result)))
    # return str(int(total_result))
    
    """
    The last line creates a string of integer in decimal, and then return it.
    """
    
    """
    Test Example print(solve(147)) 3
    """
    
    
def main():
    print("Example")
    print(solve(150)) # returns 6
    
    print("Test 1")
    print(solve(147)) # 12
    
    print("Test 1")
    print(solve(2698401)) # 2698402
    
if __name__ == "__main__":
    main()