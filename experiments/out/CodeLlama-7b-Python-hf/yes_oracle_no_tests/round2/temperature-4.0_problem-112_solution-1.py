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
	Do not include these tokens in the code: # code goes here for
	"""
    # code goes here
    ss = "".join(filter(lambda ch: ch not in c, s))
    return ss, ss[::-1] == ss


if __name__ == '__main__':
    with open('dataset_2_6.txt') as f:
        lines = f.readlines()
        s, c = lines[0].split()
        print(reverse_delete(s, c))
