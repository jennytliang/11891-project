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
    arr = [i * i - i + 1 for i in range(1,n+1)]
    ans = 0
    if n <= 2:
        return ans
    
    for i in range(1,int(n//2)+1):
        for j in range(i+1,n):
            temp = arr[i]+arr[j]
            for k in range(j+1,n+1):
                if temp % 3 == 0 and i < j < k:
                    ans+=1
    return ans

def main():
    assert get_max_triples(5) == 1 
    assert get_max_triples(8) == 2
    assert get_max_triples(3) == 0

if __name__ == '__main__':
    main()
