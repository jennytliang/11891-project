def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    
	Do not include these tokens in the code: # your code here
	"""
    # pass
    # return 0
    # remove all the zeros
    lst = [int(i) for i in lst if i != "0"]
    # remove all the numbers divisible by 2
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 2 == 0:
            lst.pop(i)
    # remove all the numbers divisible by 3
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 3 == 0:
            lst.pop(i)
    # remove all the numbers divisible by 5
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 5 == 0:
            lst.pop(i)
    # remove all the numbers divisible by 7
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 7 == 0:
            lst.pop(i)
    # remove all the numbers divisible by 11
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 11 == 0:
            lst.pop(i)
    # remove all the numbers divisible by 13
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 13 == 0:
            lst.pop(i)
    # remove all the numbers divisible by 17
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 17 == 0:
            lst.pop(i)
    # remove all the numbers divisible by 19
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 19 == 0:
            lst.pop(i)
    # remove all the numbers divisible by 23
    for i in range(len(lst)-1, -1, -1):
