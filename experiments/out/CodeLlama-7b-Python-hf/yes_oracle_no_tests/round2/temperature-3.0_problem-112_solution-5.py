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
    
	Include these tokens in the code: ss
	Do not include these tokens in the code: s = list ( s )
	"""
    #code here
    ss = ''
    for i in s:
        if i not in c:
            ss += i
    return ss, ss[::-1] == ss

if __name__ == '__main__':
    with open('dataset_7_5.txt') as f:
        s, c = f.readlines()
        s = s.strip()
        c = c.strip()
        print(reverse_delete(s, c))
