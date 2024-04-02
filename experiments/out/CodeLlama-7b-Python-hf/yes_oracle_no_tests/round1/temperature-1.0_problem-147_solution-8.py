def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    
	Include these tokens in the code: if n <=
	"""
    # A dictionary which will contain a max count of pairs of a[i] and a[j]. We use this to prune a bad sub-array.
    d = {}

    # An array which will store the results
    max_triples = [0] * n

    # A counter to calculate the number of triplets with the current size
    count = 0

    # Iterate over the array in reverse order
    for i in range(n - 1, -1, -1):

        # Iterate over all elements on the left of i; We ignore i itself
        for j in range(i - 1, -1, -1):

            # The new value of j (left part) is a[j] - (a[i] - i + 1)
            # (As j <= i; i is already included)
            new_j = i - (a[i] - a[j] - 1)

            # Check if new_j is in-scope, and lies on the left of j
            if new_j in range(j):
                continue

            # Get the max value of a[i] and a[j], which is needed to form a triplet with a[k]
            if a[i] >= max(new_j, a[j]):

                # Get count of such pairs
                count += d.get(a[i], 0)
                count += d.get(a[j], 0)
                count += d.get((a[i] + a[j]) // 3,
                               0 if (a[i] + a[j]) % 3 != 0 else -1)

        d[a[i]] = d.get(a[i], 0) + 1

        max_triples[i] = count
        count = 0

    return sum(max_triples)

# O(n) and O(1)
def get_max_triples_optimized(n):
    # We can use the same idea as in 1506
    max_triples = 0

    # Array of the length