def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    
	Include these tokens in the code: return
	Do not include these tokens in the code: upper C ases Value =
	"""
def digitSum(s):
    """Take a number, n , and print out the digits in decimal, hexadecimal, octal, and binary"""
    for s in range(0, 10):
        print("{1} {2} {3} {4}".format(bin(s), dec(s), oct(s), hex(s)))


"""Task

Given an integer, n , print the following values for each integer i from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary

The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should be space-padded to match the width of the binary value of n.

Input Format

A single integer denoting n .

Constraints

1<=n<= 2^6 (1<=n<=64)

Output Format
For each i from 1 to n, print i , the corresponding octal value of i , the corresponding hexadecimal value of i in upper case, and the corresponding binary value of i , all on the same line. Each result set should be space-padded to match the width of the binary result of n .

Sample Input 0

17

Sample Output 0
1417 2377 917F 111111001111111

"""

for n in range(1, 2**6 + 1):
        print(f'{n:10} {bin(n)[2:]:10} {hex(n)[2:].upper():>5}')
