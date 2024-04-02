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
    if len(lst) == 0:
        return 0
    else:
        for i in range(len(lst)):
            if lst[i] == 0:
                lst[i] = 2
            elif lst[i] == 1:
                lst[i] = 3
            elif lst[i] == 2:
                lst[i] = 5
            elif lst[i] == 3:
                lst[i] = 7
            elif lst[i] == 5:
                lst[i] = 11
            elif lst[i] == 7:
                lst[i] = 13
            elif lst[i] == 11:
                lst[i] = 17
            elif lst[i] == 13:
                lst[i] = 19
            elif lst[i] == 17:
                lst[i] = 23
            elif lst[i] == 19:
                lst[i] = 29
            elif lst[i] == 23:
                lst[i] = 31
            elif lst[i] == 29:
                lst[i] = 37
            elif lst[i] == 31:
                lst[i] = 41
            elif lst[i] == 37:
                lst[i] = 43
            elif lst[i] == 41:
                lst[i] = 47
            elif lst[i] == 43:
                lst[i] = 49
            elif lst[i] == 47:
                lst[i] = 53
            elif lst[i] == 53:
                lst[i] = 59
            elif lst[i] == 59:
                lst[i] = 61
            elif lst[i] == 61:
                lst[i] = 67
            elif lst[i] == 67:
                lst[i] = 71
            elif lst[i] == 71:
                lst[i]