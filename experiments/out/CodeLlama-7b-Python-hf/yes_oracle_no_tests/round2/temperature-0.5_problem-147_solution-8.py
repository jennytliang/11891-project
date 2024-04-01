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
    def is_multiple_of_3(a,b,c):
        return (a+b+c)%3 == 0
    
    def get_triples(n):
        a = [i*i - i + 1 for i in range(1,n+1)]
        return [(a[i],a[j],a[k]) for i in range(n-1) for j in range(i+1,n-1) for k in range(j+1,n) if is_multiple_of_3(a[i],a[j],a[k])]
    
    return len(get_triples(n))




if __name__ == "__main__":
    print(get_max_triples(5))
    print(get_max_triples(10))
    print(get_max_triples(100))
