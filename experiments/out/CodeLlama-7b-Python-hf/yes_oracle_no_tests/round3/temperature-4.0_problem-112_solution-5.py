def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    
	Include these tokens in the code: ss = " ". join ( filter ( lambda ch
	Do not include these tokens in the code: for char
	"""
    
    # s=input("Enter the string: ")
    # c=input("Enter the character to be removed: ")

    rev=s[::-1]
    for i in c:
        s=s.replace(i,"")
        rev=rev.replace(i,"")
    if s==rev:
        return s,True
    else:
        return s,False

if __name__ == '__main__':
    s = input("Enter the string: ")
    c = input("Enter the character to be removed: ")
    print(reverse_delete(s,c))