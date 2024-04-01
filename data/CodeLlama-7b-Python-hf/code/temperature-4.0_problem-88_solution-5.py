def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if len(array) < 2: return array
    evens = list( filter( (lambda x, idx: idx % 2 == 0), array) )
    odds = list( filter( (lambda x, idx: idx % 2 == 1 ), array ) )
    if not isOdd(sum(evens)+sum(odds)):
        return sortBySum(evens+odds)
    else:
        return sortBySum(odds+evens)

def sortBySum(array_list):
    s_array = [sum(elem) for elem in zip(array_list,array_list[0:len(array_list)//2])]
    new = [x for _, x in sorted(zip(s_array,array_list),reverse=True)]
    return new

def swapped(arr,sarr):
    sorted = True
    for i, _ in enumerate(arr):
        if arr[i] != sarr[i]:
            sorted = False
            break
        if i == len(arr) - 1 and arr[0] > sarr[0]:
            sorted = False
    return sorted

def sumisodd(sum,n):
    return isOdd( sum % n == 1, True)

def isEven(n):
   return 0 == n%2;
def isBigEven(n):
    return isOdd(n // 2)

def isOdd(num, elseValue=None):
    return (not isEven(num),0)[isEven(num[0]) if type(num) == tuple or type(num) == list else not isEven(num)] if \
            num is not None else elseValue
