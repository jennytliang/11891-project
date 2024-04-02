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
    # Initialize variables
    count = 0
    i = 1
    # Loop through all the numbers i
    while i <= n:
        j = i + 1
        # Loop through all the numbers j
        while j <= n:
            k = j + 1
            # Loop through all the numbers k
            while k <= n:
                # Check if i, j, k satisfy the condition
                if (i * i - i + 1 + j * j - j + 1 + k * k - k + 1) % 3 == 0:
                    # Increment the count
                    count += 1
                # Increment k
                k += 1
            # Increment j
            j += 1
        # Increment i
        i += 1
    # Return the count
    return count


# Driver Code
if __name__ == '__main__':
    n = 5
    print(get_max_triples(n))
