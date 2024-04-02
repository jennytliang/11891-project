def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge ( x ):
	Do not include these tokens in the code: import math result =
	"""
    ans=[]
    while len(ans)==0:
        for i in x:
            if i==0:
               break
            if (i%2 != 0) and (i%3 != 0) and (i%5 != 0) and (i%7!=0) and (i%11!=0) :
                ans.append(i)
                break
        if len(ans)<len(x):
            ans.clear()
            for i in x:
                if i==0:
                    break
                if (i%2 != 0) and (i%3 != 0) and (i%5 != 0) and (i%7!=0) and (i%11!=0) :
                    ans.append(i)
                    break
    ans.sort()
    return ans

if __name__ == "__main__":
    for i in range(1000):
        print('test', i)
        if not len(list(unique_digits([i]))) == len(list(unique_digits([i, i+1]))):
            assert unique_digits([i]) == []
