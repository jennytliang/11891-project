def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """

    # ------------------------------
    # The Ideas is similar with Questions: 1066. (DEPRECATED) Consecutive Characters, QQ 0029. Counting-Elements
    #  1) Get the frequency count first, then filter the result. 0, 1 elements have only one
    #    count, 2 elements count >= 2 and we only filter out 2 element with at MOST three numbers.

 
    def toString_CountElements(string):
        counter = collections.Counter(string.replace("0","#",k-1))
        elements = [key*num_counter for (key,num_counter) in counter.item() if num_counter >= 2 and (len(key)-2)<=1]
        return sum(elements)

    def helper(arr, start_index, tmp_list, nums, k, start_arr_val, end_arr_val, total_value, results):
        #print(arr, start_index, tmp_list, "start_arr_val", start_arr_val, "end_arr_val", end_arr_val, "nums=" + nums, "count="+ str(total_value), "max=" + str(results), sep=',')"""
        
        #if 9 < start_index: # BREAK condition: BACKTRACK INDEX > 100: len(arr)==100
        #    return

        
        #print("arr:", arr.toArray()[start_index], "index:", start_index)

        if (start_index>=len(arr)):                 # base case: check for condition to terminate back-track & return result from recursion
        
            #print(nums[2:], total_value, results) # debug
            
            try:
                results.append(int("".join(nums))) # only keep the first max valid result
            except ValueError: # ignore error for invalid num string, like: 44656560
                pass                
            return # backtrack & return
        
        try:    # if input string is invalid (not only digits), throw error & terminate
            arr.remove(start_array_val)
            print(arr, start_arr_val)
            start_index -= 1
            arr.append(start_arr_val) # Backtracking
            #input("enter any key to continue ....")
        except ValueError:    # ignore invalid num string, such as: arr=[0.192, ..., ..], nums=[2,2,2,3333,
            #input("enter to continue.....")
            pass                  # skip the invalid input in the first place    

    
        start_index += 3
        # for nums:  (9,30,59,53,14,33,9,9,2,0,9)=[], (9,24,79,72,18,38,9,17,7,0,19)=[] for case=1: 
        # check for first 3 elements that is in range of 33~99, else, find the 3 consecutive elements in list that add up to be 99:
        if arr[start]< 100 or (len(total_ele_list) and arr[start+1]+sum(ele) <=99199): 
        # 1. if (len(elements)==3) and (sum(list[ele])<=100) 
        #  - then (start_ele-1) -> check for index of 3 consequent ints >= 2 digits:
        #    > if 0, or (list[start]+ ele_list[0] <=199 or (ele[1]+ele2[0]))<=909, append to list.
            nums.append((start_index-100) +1) # 
            ele0 = str(start_array_val)
            ele1 = "".join(ele)        
            ele2 = nums[-1]                  
            total_value += int("19"+ ele1 + ele2)  
            return # back track
        elif 3<=len(inputs)<=