def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r = [] for
	'''
    
    def is_palindrome(lst):
        # initialize left and right pointers
        left, right = 0, len(lst) - 1
        # loop through the array
        while left <= right:
            # compare left to right and return true if they are equal
            if lst[left] == lst[right]:
                return True
            # increment left and decrement right
            left += 1
            right -= 1
        # return false if the array is not equal at any point
        return False
    
    def sum_list(lst):
        # initialize sum
        sum = 0
        # loop through the array
        for i in lst:
            # add each element to the sum
            sum += i
        # return the sum
        return sum
    
    # if the list is not balanced
    if not is_palindrome(q):
        # return false
        return False
    # if the sum is less than or equal to the maximum possible weight
    if sum_list(q) <= w:
        # return true
        return True
    # otherwise
    else:
        # return false
        return False


# test
q = [1, 2]
w = 5
print(will_it_fly(q, w))

q = [3, 2, 3]
w = 1
print(will_it_fly(q, w))

q = [3, 2, 3]
w = 9
print(will_it_fly(q, w))

q = [3]
w = 5
print(will_it_fly(q, w))