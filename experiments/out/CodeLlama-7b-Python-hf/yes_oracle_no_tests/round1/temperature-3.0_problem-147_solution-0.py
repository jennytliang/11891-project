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
    # Initialize a list of the first n+1 natural numbers
    # For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1
    a = [i * i - i + 1 for i in range(1, n + 1)]
    # Set the count to zero
    count = 0
    # Iterate over the array
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # If a[i] + a[j] + a[k] is a multiple of 3, increment count
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    # Return count
    return count


# Get the number of triples
triple_count = get_max_triples(5)
# Print the number of triples
print(triple_count)
