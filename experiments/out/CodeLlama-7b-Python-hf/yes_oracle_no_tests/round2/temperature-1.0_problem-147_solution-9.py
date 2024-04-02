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
    
    ###############################
    # Determination and counting of valid solutions in an array of a such that:
    #    is multiple of 3
    #    is not in sorted order
    
    # Solution 1: brute-force method
    # def get_numbers_within_three(n):
    #     """"
    #     Return the number of numbers in 1 .. n such that is multiple of 3
    #     """
    #     counter = 0
    #     for ind in range(1, n + 1):
    #         if ind % 3 == 0:
    #             counter += 1 # ind is multiple of 3   
    #     return counter    
    
    # Solution 2:
    # Return the number of numbers in 1 .. n such that is multiple of 3
    def get_numbers_within_three(n):
        return (n // 3) + (n % 3)
    
    # determine the number of non-decreasing triples a[i], a[j], a[k] of a such that
    #  a[i] is multiple of 3
    #  sorted order => 2 <= i <= j <= k
    #  is not in sorted order => j < k
    def get_number_of_triples(n):
        return ( n * (n - 1) * (n - 2)) // 6 # max(j - i, k - j + 1) = 2 for any i, k
    
    # determine the number of non-decreasing triples a[i], a[j], a[k] of a such that
    #  a[i] is multiple of 3 
    #  a[i], a[j], a[k] are in ascending order 
    #  k - j = 2 
    def get_number_of_triples_monotonic(n):
        return ( n * (n - 1) // 2 ) # max (k - j) = 2 for any i, n 
    
    # number of triples = 1 + (number of