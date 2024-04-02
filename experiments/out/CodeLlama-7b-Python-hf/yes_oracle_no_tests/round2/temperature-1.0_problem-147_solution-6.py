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
    
	Do not include these tokens in the code: arr = [ i * i -
	"""
    
    def get_max_triples(n):
        nums = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(1, i):
                a, b = nums[i-j]+nums[i]+1, nums[i]
                b = b**2 - b + 1
                nums[i] = a
                return nums[-1]


def main():
    for _ in range(int(input())):
        n = int(input())
        res = get_max_triples(n)
        print(res)
    

if __name__ == "__main__":
    main()
