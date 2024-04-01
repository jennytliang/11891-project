def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # for i in l: # for every number i in the list l...
    #     for e in l[ l.index(i)+1 : ]: if i+e is 0 return True. # loop over all items in the list l from i to its end...  if there is any item e in the list... which makes item i and e equal 0 (additive inverse of item i) then...

    # #  for any number i... if there are 3 distinct items that sum to make i and 7 then...  #  check if for any item x.. there is any item in the list that adds up to 8 (7 and [any item]) #  return false

    #  If the sum of the two numbers sum to 8, return false, or if the list of length 2 has one value, it is false
    #  1) We are going to go through each element in our list
    # l for every number [item 'i'] in l ...
        # for every [item [ 'e'] following item 'i']
       #  if the sum of the items, 'i' and 'e' is ZERO
          # then we found the answer, return True # if two items match in value, but their order are opposite, we will end up returning True # 
        #   # if any item in the list adds to zero:

           # #  For any item [e], we are looping over an item in the list after 
            # the item i, then 

        #  # if the two items, i and the item e, the two sum to ZER
            # return true
            # print("We found the sum is zero for item: 'i'")  # this should only happen for 2 items, and return True only if these 2 items sum to 7 and 7
            
    

  
