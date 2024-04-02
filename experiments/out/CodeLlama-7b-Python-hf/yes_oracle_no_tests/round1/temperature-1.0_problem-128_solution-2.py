def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: len ( )
	"""

  if len(arr) == 0:
    return None
  else:
    for val in [1, -1]:
      if arr.count(val) % 2 == 1:
        arr.insert(arr.count(1) + arr.count(-1)
                   , -1 if val == 1 else 1)
    return (prod := 1 \
      if arr[0] == 1 \
      else arr[0]) \
      * (sum(arr) / prod)

print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))

# def prod_signs(arr):
#     total = 1
#     for val in [1, -1]:
#         if arr.count(val) % 2 == 1 and val != total:
#             arr.insert(arr.count(1) + arr.count(-1), -1 if total == 1 else 1)
#         total = -1 if total == 1 else 1
#     return sum(arr) if arr[0] == 1 else -sum(arr)


# if __name__ == '__main__':
#     a = list(map(int, input().split()))
#     print(prod_signs(a))

# def num_signs(arr):
#     for val in [1, -1]:
#         if arr.count(val) % 2 == 1:
#             arr.insert(arr.count(1) + arr.count(-1)
#                        , -1 if val == 1 else 1)
#     return arr.sort()

# arr = [1, 2, 2, -4]
# print(num_signs(arr))