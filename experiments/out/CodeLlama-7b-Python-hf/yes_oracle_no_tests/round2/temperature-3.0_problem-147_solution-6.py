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
    # Initialize count
    count = 0
    # Iterate over each number till n
    for i in range(1,n+1):
        # Square the number
        num = i*i
        # Subtract 1 from it
        num = num - 1
        # Add 1 to it
        num = num + 1
        # Multiply the num by 3
        num = num * 3
        # If num is a multiple of 3
        if num % 3 == 0:
            # Increment the count
            count += 1
    # Return the count
    return count

if __name__ == "__main__":
    n = 5
    print(get_max_triples(n))
