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
### SOLUTION ONE ###
    # get sum as a number
    sums=sum(map(lambda x: int(x), bin(N)[2:]))  # remove '0b' from start: bin() function appends '0b' as prefix
    # convert number sums to a binary string: bin()
    return bin(sums)[2:]  

### SOLUTION TWO ###
    # using lambda, return the binary representation of each digit in n, convert string to a number (int()), return that number to 'sums', add it to an empty list, and return a string of the sum (bin)
    sums=list(map(lambda x : int(bin(x)[2:]), str(N)[::-1]))
    sums=str(sum(sums))[2:]
    return sums