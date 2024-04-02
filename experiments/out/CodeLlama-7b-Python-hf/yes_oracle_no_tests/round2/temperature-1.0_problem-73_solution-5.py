def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: # create a dictionary with
	"""
    # create a dictionary with number as keys and a list of all
    # indices that have that number
    # so the dictionary looks something like {'1' : [0, 3, 5], '2' : [1, 3], '3': , ...}
    # where '1' is stored as ['1',0,3,5], where numbers == [num,index,index,index...]
    # '2' has indices [1,3], and so on...
    
    # I'm assuming that the input array will look like:
    # arr = [1,2,3,4,5]
    # and not like
    # arr = ['a','b','c','d','e']
    # or 
    # arr = [1, 1, 2, 3, 4]
    # We're supposed to make this into a palindrome
    # but the most efficient way of doing that is to start
    # at both ends....
    '''
    left = 0
    right = len(arr)-1
    counter = 0
    while counter < len(arr) / 2:
        if arr[left] != arr[right]:
            if arr[left] == arr[right] - 1:
                arr[left] = arr[right]
        counter += 1
        left += 1
        right -= 1
    return counter
    '''
    # this is what my professor gave us as the answer
    # we were supposed to solve it on paper first in about 8 minutes
    # so this is just what we're solving the problem...
    # using O(n) time and O(1) space
    
    # this assumes that, unlike
    # arr = ['a','b','c','d']
    # we just have a basic list of numbers
    # in that case, the answer would be 0
    
    # we could get an answer by just looking at the middle...
    # but sometimes the middle of the array won't contain each
    # of the numbers
    # arr = [1, 2, 3, 4]
    # the middle isn't the right answer...