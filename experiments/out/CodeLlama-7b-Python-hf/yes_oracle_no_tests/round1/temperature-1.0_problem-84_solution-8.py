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
    
    return bin(sum(map(lambda x: int(x), list(str(N))))))[2:]


# N = 981069 # the answer should be ['1001010101000010101']
# N = 1912 #the answer should be ['1101100001010']
# N = 10005352 #the answer should be ['101101001101011000001101100']
# N = 19432 #the answer should be ['1111000110110010110']
# N = 8418 #the answer should be ['1001100111000']
# N = 2894 #the answer should be ['100011111']
# N = 31 #the answer should be ['3']
# N = 18238671321263516962308603626144599341062594317945190 #the answer should be ['1111
