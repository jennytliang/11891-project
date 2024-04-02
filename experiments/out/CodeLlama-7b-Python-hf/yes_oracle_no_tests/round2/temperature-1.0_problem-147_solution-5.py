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
    # count = 0

    # for i in range(1, n, 2):
    #     s = i * i - i + 1
    #     if s % 3 == 0:
    #         count += 1


    #     for j in range(n):
    #         if s+j % 3 == 0:
    #             pass
    # for i in range(0, n):
    #     pass


def sub(a, b):
    """
        Input_A: Tuple(int)
        Output_A: 1
        Input_B: Tuple(int)
        Output_B: 1
    """
    # Write your main code here
    a[0], a[1], a[2] = a[0] + a[1], a[0] + a[1] + a[2], a[1] + a[2]
    return a, a[::-1]

def findSubArray(arr, a):
    # Your code goes here
    arr2 = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sum(arr[i:j]) == a:
                arr2.append(arr[i:j])


def findPair(arr1, b):
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            if (arr1[i] + arr1[j]) == b:
                return i, j

def findTwoNum(arr1, b, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] + arr2[j] > b:
                pass




if __name__ == "__main__":
    n = 2
    # result = get_max_triples(n)
    # print(result)
    arr = (1,2,3,4,5)
    b = 4
    # a, b = findSubArray(arr, 5)