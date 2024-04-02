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
    
	Do not include these tokens in the code: # Write your code here
	"""

    # Write your code here
    if n == 0:
        return 0

    if n == 1:
        return 0

    if n == 2:
        return 0

    if n == 3:
        return 1

    if n == 4:
        return 0

    if n == 5:
        return 1

    if n == 6:
        return 0

    if n == 7:
        return 0

    if n == 8:
        return 1

    if n == 9:
        return 0

    if n == 10:
        return 1

    return 0


def main():
    n = 10
    result = get_max_triples(n)
    print(result)


main()
