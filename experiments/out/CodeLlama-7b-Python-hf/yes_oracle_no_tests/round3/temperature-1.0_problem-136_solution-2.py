def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    
	Include these tokens in the code: neg = list
	Do not include these tokens in the code: # 2 . Return largest negative
	'''
    # 1. create a function with the given parameters
def largest_smallest_integers(lst):
    # 2. create a list called neg to hold the negatives
    neg = []
    # 3. create a list called pos to hold the positives
    pos = []
    # 4. create a variable called largest to hold the largest negative
    largest = None
    # 5. create a variable called smallest to hold the smallest positive
    smallest = None
    # 6. create a for loop that iterates through each item in the given list
    for item in lst:
        # 7. if the item is negative, append it to the neg list
        if item < 0:
            neg.append(item)
        # 8. if the item is positive, append it to the pos list
        if item > 0:
            pos.append(item)
    # 9. create an if statement that checks if the neg list is empty
    if neg == []:
        # 10. if it is, return the largest as None
        largest = None
    # 11. if it is not, create a for loop that iterates through the neg list
    for item in neg:
        # 12. create an if statement that checks if the item is larger than the largest
        if item > largest:
            # 13. if it is, store it in the largest variable
            largest = item
    # 14. create an if statement that checks if the pos list is empty
    if pos == []:
        # 15. if it is, return the smallest as None
        smallest = None
    # 16. if it is not, create a for loop that iterates through the pos list
    for item in pos:
        # 17. create an if statement that checks if the item is smaller than the smallest
        if item < smallest:
            # 18. if it is, store it in the smallest variable
            smallest = item
    # 19. return the largest and smallest variables
    return (largest, smallest)
    # 20. return a tuple of the largest and smallest variables

# 21