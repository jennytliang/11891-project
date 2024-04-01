def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 0:
        return 0
    currSum = sum(nums)  # if everything is negative, just use 2 pointers and return min value over that subarray
    # if there aren't any negatives it's the min value
    minSum = float('inf')

    for pointerEnd in range(len(nums)):
        minSum = currSum
        for subarray in range(1, len(nums)):
            first = nums[:subarray]

            if subarray <= pointerEnd:
                first = nums[pointerEnd -
                             subarray: pointerEnd] if subarray-1 <= pointerEnd-subarray//2 else nums[subarray: pointerEnd]
            elif subarray == pointerEnd:
                return pointerEnd
            currSum = minSum

            minSum = currSum if subarray <= pointerEnd else min(
                currSum, sum(nums[:(pointerEnd)]))

    return min(currSum, min(nums))


"""
def get_lead(arr, m, n, k, p, lead_score):
    # Base case
	# If team is eliminated
	if n <= k: return arr[0][1]

	# Check if there exists a team that leads by more than k wins
	for i in arr[m:]:
		if i[1] > lead_score - k:
			# Eliminating the teams up to next index
			res = min( 
				get_lead(arr, m, n, k-i[1], (p-1)/i[0], i[1]-k) + i[1],
				# Get the k-th place or last team from rest of the tournament
    			get_nth_place(arr, n, 2, k)
			)
			return res - k

    # If all teams win
	# Returns the best of last kth place or last first place(which will always be the last if less than k teams)
	# The idea here is to add k to all results from rest of tournament as there is a k gap between the team finishing
    # in last and kth place
    # (1) a team that gets eliminated will return res - k because the teams after it have already counted k games
    # and then we added k to what they won, which gives back all games it had including the eliminated k-games
    # OR
	# (2) if there are less than k wins for any team, adding k will not affect any result from the rest of tournament and
	return min(-lead_score, # k-games were lost
		# we will always be able to eliminate at last k-places if there are less than or k teams left
		get_others_lead(p/arr[m][0] - 1) if m <= p else arr[-k][1]
	      + k       # k-games will be gained since all games have a gap of k-games and
	)   
"""        