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
    
	Include these tokens in the code: def digits ( x : int ) -> int :
	"""
    from collections import Counter
    
    # O(kN) Time and O(N) Space, where k is the number of elements to be considered, and N
    # is the input size.
    # It seems pretty optimal, but a more accurate analysis should be done.
    def add_elements_optimized(arr, k, sum3 = 0, i = 0):
        if i == k:
            return sum3
        x = arr[i]
        s = sum3 + x 
        if x >= 10 and x <= 99:
            return s 
        m1, m2, m3, m4 = x // 100, x // 10 % 10, x % 10, 0
        if m1 == m2 == m3 and m1 > 0:
            return s
        else:
            if m1 == 1 and m4 == 0:
                sum3 += x % 10
            elif m2 == 1 and m4 == 0:
                sum3 += x % 100
            elif m4 == 1:
                sum3 += x
            sum3 = add_elements_optimized(arr, k, sum3, i + 1)
            return sum3 

    # O(kN) Time and O(N) Space, where k is the number of elements to be considered, and N
    # is the input size.
    # Again, this seems to be the way to go to me.
    def add_elements_optimized_2(arr, k, sum3 = 0, c = Counter()):
        if k == 0:
            return sum3 
        else:
            for x in arr:
                s = sum3 + x 
                if x > 100 or x < 10:
                    sum3 = add_elements_optimized_2(arr, k - 1,  s, c)
                elif x <= 99:
                    c[x] += 1
                    if x % 10 == 1 and c[x % 10] == 2: