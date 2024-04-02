def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: from fun ct ools import c mp _ to _
	"""
    result = [None] * len(arr)
    for n in arr:
        one, others = bin(n).split('1')[0], bin(n).split('1')[1]
        try:
            result[int((len(ones) - len(others)) * 1000)] = n
        except:
            continue
    return result
    # result = [int((len(bin(n).split('1')[0]) - len(bin(n).split('1')[1])) * 1000), arr.append(n)]


def sort_array_solution(nums):
    buckets = {}

    for i in range(len(nums)):

        ones, b = 0, ''
        while nums[i] > 0:
            b = str(nums[i] % 10) + b
            nums[i] //= 10

        while len(b) < 31:
            b += '0'

        ones = b.count('1')

        if not buckets.get(ones, None):
            buckets[ones] = []
        buckets[ones].append(nums[i])

    flatten = lambda ll: [j for i in ll for j in i]
    return flatten(buckets[i] for i in sorted(buckets))


def sort_array_solution_2(arr):
    index = 0
    l = len(arr)

    for i in range(l):
        if 0 == arr[i]:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1

    for i in range(index, l):
        for j in range(index, i):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

    return arr

