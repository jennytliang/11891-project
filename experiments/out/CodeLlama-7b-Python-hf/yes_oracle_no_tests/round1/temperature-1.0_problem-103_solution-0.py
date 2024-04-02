def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    
	Include these tokens in the code: av g = round (( n + m ) /
	"""

    if n > m:
         return None
    
    avg = round((n + m) / 2)
    binAvg = bin( avg)

    return binAvg
    

    return None


def all_the_same(lst):
    """Given a non-empty list of integers lst, return a string that contains three 
    integers where the two middle integers are the same,and the last integer is the 
    same as the first. The list is guaranteed to have at least three integers.
    Examples:
    
    non_repeating([1, 1, 1, 1]) => 111
    non_repeating([1,2,3,1]) => 121
    non_repeating([6, 8, 10, 6, 12] ) => 686
    
    """
    if lst[0] == lst[1] and lst[1] == lst[2]:
        return lst[0]*3

    if lst[0] == lst[1] and lst[1] != lst[2]:
        return lst[0]*2 + lst[2]
    
    if lst[0] != lst[1] and lst[1] != lst[2]:
        return lst[0] + lst[1]*2

    if lst[0] != lst[1] and lst[1] == lst[2]:
        return lst[0]+lst[1]+lst[0]
    
#    return None


def check_subset(sub, big):
    """Given two non-empty arrays A and B, and an integer X, check whether A can be partitioned 
    into three subsets of  integers such that the sum of elements in each of the  two  subsets 
    plus the sum of X amounts exactly to the array B.
    Examples:
    partition([1, 3, 7, 9], [2, 4 ,8], 13 ) => -1
    partition([1, 3, 7, 9], [2, 4 ,8], 9 ) => [1,3,7]
    partition([2