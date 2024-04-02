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
	"""
    
    upperCasesValue = sum([ ord(c) for c in s if c.isupper() ])
    
    return upperCasesValue
	
	
	
def digitSum1(s):
	"""Task
    Write a function that takes a string and returns the sum of the upper characters only'
    ASCII codes.
	There are many ways to solve this task. 
	You can use either if, for, while solution.
	You can use slicing to get subparts of the string.
	You can use list comprehension and sum function.
	You can create a dictionary.
    Have fun!

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153

    """
	sum = 0
	for i in s:
		if(ord(i) >= 65 and ord(i) <= 90):
			sum+=ord(i)
	return sum
	
if __name__ == '__main__':
    print(digitSum1(""))