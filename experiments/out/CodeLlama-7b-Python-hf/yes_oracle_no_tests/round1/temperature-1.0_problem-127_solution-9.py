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
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    a,b,c,d=interval1
    e,f,g,h=interval2
    if a>b or a>e and c>f: return "NO"
    if b<e and a<=e and c<=f:
        a,b,c,d=e,f,a,b
    start=max(a,e)
    stop=min(b,f)
    set1=set(range(start,stop+1))
    while start<=stop:
       if c>b or c>h: return "NO"
       if start<=c and start<=h and stop>=c and stop>=h: return "NO"
       if c<=start and c<=stop: break
       start+=1
    if start in set1: return "YES"
    else: return "NO"
