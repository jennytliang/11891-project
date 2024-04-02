def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    
	Include these tokens in the code: ans , num = [], n
	"""
    
    # Create an empty list to store stone's number in each level(ans)
    # Create an integer var to store n, input argument given to the function by user(num)
    ans = []
    num = 0

    # Given that num (i.e. num of stones to build) is the argument in function
    # We need to add the next odd number if n is even 
    # We need to add the next event number if n is even

    # Add the value of num to ans list.
    ans.append(num)
    # Add increment value of the num to ans list.
    ans.append(num + 2)
    # Iterate over n-1 time and add incramented value to ans list.
    for _ in range(n - 2):
        num += 4
        ans.append(num)
        
    return ans



if __name__ == '__main__':
    import doctest
    doctest.testmod()
