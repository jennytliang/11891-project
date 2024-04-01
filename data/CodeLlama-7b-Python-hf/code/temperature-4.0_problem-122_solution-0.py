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
        