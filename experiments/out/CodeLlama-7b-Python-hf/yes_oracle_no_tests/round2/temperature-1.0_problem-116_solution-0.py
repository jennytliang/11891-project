def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: from fun ct ools import
	Do not include these tokens in the code: # return sorted ( #
	"""

    bins = {}

    for i in arr: # split into "1" arrays and store in separate list within a dictionary
        dec_str = str(bin(i)) 
        count = str(dec_str).count('1')
        if len(dec_str)-2 not in bins.keys(): # no 0s! 
            bins[len(dec_str)-2] = []
        bins[len(dec_str)-2].append(i)

    # print(bins)  # # check it's working 
    # print(list(bins.values())) # # check it's working 
    
    # order the lists by 1s descending, to get high values last. Then 2nd order by 2nd descending, 3rd by 3rd descending and so on!  
    for i in range(len(bins)): # order the lists by 1s descending
        bins[i] = sorted(bins[i], key=lambda x: bin(abs(x)), reverse=True)  
        for j in range(len(bins[i])): # order again by absolute value (if two lists have the same number of 1s, the bigger absolute value is first)
            bins[i][j] = abs(bins[i][j])

    # print("after")
    # print(bins) # check it's working 
    # print(list(bins.values())) # check it's working
    
    # change the dictionary back to a list   
    sorted_list = []
    for i in list(bins.values()): # order the lists of sorted lists by 1s descending
        sorted_list += i
        # print(list(bins.values()))

    return sorted_list
