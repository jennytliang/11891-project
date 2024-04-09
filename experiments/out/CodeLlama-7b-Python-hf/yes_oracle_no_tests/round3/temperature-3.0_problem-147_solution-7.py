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
    pass


def get_max_triples_soln(n):
    """
    Solution:
    * Count the number of numbers that are multiples of 3
    * Count the number of numbers that are multiples of 5
    * Count the number of numbers that are multiples of 15
    * Count the number of numbers that are not multiples of 15
    * The number of triples is sum of all of these
    """
    # Check for n <= 0
    if n <= 0:
        return 0

    # Initialize count of multiples of 3, 5, 15
    count_3 = 0
    count_5 = 0
    count_15 = 0

    # Iterate from 1 to n and count multiples of 3, 5, 15
    for i in range(1, n+1):
        if i % 3 == 0:
            count_3 += 1
        if i % 5 == 0:
            count_5 += 1
        if i % 15 == 0:
            count_15 += 1

    # The total number of triples is sum of all of these
    return count_3 * (count_3 - 1) // 2 + count_5 * (count_5 - 1) // 2 + count_15 * (count_15 - 1) // 2


# print(get_max_triples_soln(5))
# print(get_max_triples_soln(12))
# print(get_max_triples_soln(0))
# print(get_max_triples_soln(1))
# print(get_max_triples_soln(2))
# print(get_max_triples_soln(3))
# print(get_max_triples_soln(4))
# print(get_max_triples_soln(5))
# print(get_max_triples_soln(6))
# print(get_max_triples_soln(7))
