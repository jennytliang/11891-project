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
    # Initialize the count
    triple_count = 0

    # For each i, j, k
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                # Check if sum of i, j, k is a multiple of 3
                if (i + j + k) % 3 == 0:
                    # Increment the count
                    triple_count += 1

    # Return the count
    return triple_count


if __name__ == "__main__":
    n = 5
    result = get_max_triples(n)
    print(result)
