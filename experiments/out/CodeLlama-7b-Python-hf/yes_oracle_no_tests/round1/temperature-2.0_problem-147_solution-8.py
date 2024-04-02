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
    # Initialize result
    result = 0
    
    # Loop through each number
    for i in range(1, n+1):
        # Square the number
        num = i * i - i + 1
        
        # Check if num is divisible by 3
        if num % 3 == 0:
            # Increment result
            result += 1
            
    # Return result
    return result

# Get the number of triples
result = get_max_triples(5)

# Print the result
print("The number of triples is " + str(result))