def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    
	Include these tokens in the code: num
	Do not include these tokens in the code: i
	'''

    count = dict()
  
    # counting the frequency of each number
    for num in lst:
        count[num] = count.get(num, 0) + 1
  
    # searching for the number with frequency greater than or equal to the number itself
    for num in lst:
        if count[num] >= num and num > 0:
            return num
  
    return -1

def test(candidate, expected):

    # Some hints on how to test your solutions.
    #   You'll need to test with invalid inputs as well.
    #   You'll need to test with a very large input as well.
    assert candidate([4, 1, 2, 2, 3, 1]) == expected
    assert candidate([1, 2, 2, 3, 3, 3, 4, 4, 4]) == expected
    assert candidate([5, 5, 4, 4, 4]) == expected

if __name__ == '__main__':
    test(search, 2)
