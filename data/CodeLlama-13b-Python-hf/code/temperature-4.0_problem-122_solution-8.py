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
    if not k:
        return 0
    elif arr and len(arr) > 1:
        sum_of_elens = sum([len(str(i)) for i in arr])

        # Find the index we can reach without going over our summation limit. All
        # indices after our limit will add nothing to the current sum we're at, hence
        # can be ignored. There is an optimization where we set our idx to k when k
        # reaches the current sum limit. But the first loop is to set up for this k
        # to be reached in, so we can't initialize it in this spot
        count = 0
        idx, s = 0, (arr[0] if len(arr) - 1 else sum_of_elens)
        max_limit_sum = sum_of_elens - k

        for i, el in enumerate(arr):
            # When our sum reaches a certain point (we can call it our index), it means
            # that the elements from our index after will add nothing. Optimization: idx to k when k
            # reaches current sum limit. So, we set up for the second loop to start at this idx.
            # idx, k = i, (0 if idx == k else k - i) # Optimized

            if i + 1 < k:
                if i == 0:
                    idx = 1
                elif i == idx: # when idx == 0, means we reached a limit, hence our count has not changed. otherwise, we want to continue with our sum from this i. This is because our idx was reached with another sum that was not reached with this idx - hence the reason to move forward, to reach the next valid number with our sum limit of 3 digits. See below for another example with more details.
                    idx = count
                s += el
                count = i if i == idx else count
                if count > 0 and s - arr[count - 1] > max_limit_sum: # since we are in a while loop, it is equivalent to `elif` (it's either the if condition from the loop above, or the condition below in the else), but I just want to point it out for convenience. count will keep changing until it reaches another element with a difference below our max limit sum. We also want to keep increasing our idx since we know that the numbers before idx are already too large since our max sum only decreases in every iteration after we reach the next number within the limit
                    idx += 1


        # print(s, k - i) # s should now be within the k count

        sum_two_digits, two_digits, idx, k, count = 0, 0, idx, (k if k == 0 else len(arr) - k) + idx, len(arr)
        while len(arr) >= idx:
            if k > 0 and sum_two_digits <= max_limit_sum + k:
                if idx > count:
                    idx = 1

                idx = count if count != 0 else idx + 1
            elif k <= 0 and idx + 1 < len(arr):
                # Since we are on the last index, count must reach its final value. If idx == k, than that means we only reached k with the first if statement, but on the next while loop the k becomes 0 so it goes to the next if statement and idx becomes 1. But if we do continue, then we may go below the index of our largest element which is count
                if idx > count - 1:
                    idx = sum([count, 1])
                    idx = idx + 1 if k < 0 else idx

            if idx > 0:
                sum_of_elens -= len(str(el))
                # If we haven't exceeded, we want to check again, otherwise, our two digits will end on this index, so we have to decrease the next largest element by one so that we reach the required index, then end the loop, hence add the sum, which is done by the else clause
                if sum_two_digits + sum([k, sum_of_elens]) <= max_limit_sum or k == 0:
                    sum_two_digits += el
                # else:
                #     k = el
            else:
                # k has already been decremented by one, hence not necessary
                # k -= 1
                count -= 1

            # This is only if the last index of our input array is 9 and we reach our max limit before our count gets to the next one. This is necessary to increase the idx so we can loop again and break out before we reach the count
            if idx == len(arr) - 1 and count < idx:
                if count > idx:
                    count = idx
                count += 1

            # This is only necessary when we have reached our limit and our idx starts at a certain non-zero element. This is to reset our index so that we no longer count it when we want to check our next two elements since they will already be below the limit
            if count <= idx and count != 0 and len(arr) != idx and not (idx > k and count < idx): # the latter condition will be necessary if we reach count as 0, but idx doesn't = k and the index is not the largest element, hence we have to ignore it. It seems like we are not at the count of our max limit when we reach count==0. To see why, printout the count. It will be different from the current idx so we need to fix our idx and count and continue to loop again to reach the same element with a difference of zero and to be within our max limit sum since the latter element is already added and not included in our count
                count = 0
            # This else is only necessary if the loop is done when we are in a larger index and not within our limit. This will update our idx to be a valid index with valid number to continue with. This is so we could keep checking for the next valid index when we hit our limit and no other elements within it satisfy our condition. This is so we do not stop and do not include the value of this index. Otherwise, we may go to a certain idx, but not satisfy our k requirement. Then it goes to the same idx again. Since it has already passed, we can just update it and check again, which is what the following while loop will do. This else block will fix the problem with this. This if and else statement are to keep increasing the idx so it never goes to a negative index since the latter statement is not inclusive for idx and if we reach 1, it will not break out because the sum of digit lengths will still not be less than max sum. This will happen if the next element is not in the limit. But we need to have k>0 or else the next if and else will not be included hence we'll loop around again for no reason, as we want to go through every element. If k==0, then it is guaranteed we will reach the last index since we never decrement our k and the idx will continue to increment since count>idx. We will loop around again, except that we would be in the previous element which we would have already checked with our maxSum limit. So no need to loop again. So k==0 is special. We want to break here since this means our previous idx had to have reached a max digit count. Hence, the next idx should be equal to our previous max limit sum of 2 digits. But if it is the same as that of max limit, that means that this is already our max limit and we can just return it. This is the very last statement that is special
            elif idx == count - 1 and k >= idx: # We would have already reached this condition if idx == count without this else if statement, because we set it as count. This will increase our idx again so that we also keep checking the next valid number that we are looking for
                while idx == count: # we can also do it like this but I find this cleaner
                    idx += 1; # if idx <= 0: print(arr[idx] == 9, idx); # when idx=6 and k is 1, we'll hit the first if statement and then again in the else if statement but we need to make this a while loop and keep increasing idx. Otherwise we won't find the next number after idx=6 in our input array that meets the criteria of <=3 digits

                if i == len(arr)-1 and idx > 2*arr[i] < k: # If our index starts at count or count+1, we may go to the last element again. We can safely skip it since its digit is already counted in the last count, and hence this will give us an index we can reach within the limit. We have to account for 2 digits though if k == len(arr). This else block will not be reached any more once