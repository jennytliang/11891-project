def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge ( x : int ) -> int :
	"""
    
    sign = 0
    neg = 0
    for i in arr:
        num = abs(i)
        snum = str(num)
        for j in snum:
            sign += (ord(j) - 48)
        if i < 0:
            neg += 1
        else:
            if sign > 0:
                arr.append(i)
    arr.sort()
    return (len(arr) - neg)
    
    return sum - neg
 
 
def count_nums_2(arr):
    a = [1 for n in arr if sum(int(a) for a in str(abs(n))) > 0 or n < 0]
    return len(a) - a.count(0)
 
 
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(count_nums(arr))
