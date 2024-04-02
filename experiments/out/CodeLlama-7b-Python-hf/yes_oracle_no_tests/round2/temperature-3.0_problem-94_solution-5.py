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
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    lst = [x for x in lst if x != 0]
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0 or lst[i] % 3 == 0 or lst[i] % 5 == 0 or lst[i] % 7 == 0:
            lst[i] = 0
            i += 1
        else:
            i += 1
    lst = [x for x in lst if x != 0]
    lst = [x for x in lst if x != 1]
    lst = [x for x in lst if x != 2]
    lst = [x for x in lst if x != 3]
    lst = [x for x in lst if x != 5]
    lst = [x for x in lst if x != 7]
    lst = [x for x in lst if x != 11]
    lst = [x for x in lst if x != 13]
    lst = [x for x in lst if x != 17]
    lst = [x for x in lst if x != 19]
    lst = [x for x in lst if x != 23]
    lst = [x for x in lst if x != 29]
    lst = [x for x in lst if x != 31]
    lst = [x for x in lst if x != 37]
    lst = [x for x in lst if x != 41]
    lst = [x for x in lst if x != 43]
    lst = [x for x in lst if x != 47]
    lst = [x for x in lst if x != 53]
    lst = [x for x in lst if x != 59]
    lst = [x for x in lst if x != 61]
    lst = [x for x in lst if x != 67]
    lst = [x for x in lst if x != 71]
    lst = [x for x in lst if x != 73]
    lst = [x for x in lst if x !=