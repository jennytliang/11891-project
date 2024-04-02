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
    s = ''
	
    if N > 0:
        for i in range(1,N+1):
            if N > 1:
                s = s + bin(i)[2:]
            else:
                s = bin(i)
        return sum(list(map(int,list(s))))
    else:
        return N
        
def main():
    data = [1000, 150, 147, 1334, 3232, 232312, 12312]
    
    for d in data:
        print('Input data: ', d)
        print('Output: ', solve(d))

if __name__ == '__main__':
    main()

