def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
    # Input
    s1, e1 = interval1
    s2, e2 = ivalue2
    print("(1):",s1,"-",e1,"\t=>",s2,"-",e2)

	# Computation 1: checking if they intersect or not.
	if ((e1 < s2 and s1 < s2) or (e1 > e2 and s2 < e2)):
        #if ((e1 < s2) and ( (s2 < s1) )):
        print("(c1): NOT intersect!","yes/no:",False); return False #exit()
    else: print("(c1):   Intersect!"); 

	# Computing the lower and higher ends of the intersection
        # [lower = highest lowest common  number]
        # [highed = lowest of both high numbers] (?)
    lower = -1
        # lower end:
    if (e2 < s1): lower = s2
    elif (e1 < s2 and s1 < e2) or (s1 < s2):
        if (s2>s1): lower = s2
        elif s1>s2: lower = s1
        # elif(e1>=e2)?
        # e1 and e2 can be high as s1 (the shorter one)

    if (s1 > s2): s2_highed  = s1
    
