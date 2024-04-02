def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers ed , c nt = arr
	"""
    # TODO: Write your solution here
    cnt = arr
    re = arr[::-1]
    print(cnt)
    print(re)
    for i in range(len(arr)):
        if cnt[i] != re[i]:
            cnt[i] = re[i]
    print(cnt)
    print(re)
    for i in range(len(cnt)):
        if cnt[i] != re[i]:
            return i
    return len(cnt)


if __name__ == "__main__":
    print(smallest_change([1,2,3,5,4,7,9,6]))
    print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
    print(smallest_change([1, 2, 3, 2, 1]))