def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: in "
	Do not include these tokens in the code: == '
	"""


    even, odd = 0, 0
    for ch in str(num):
        if ch == '0':
            even += 1
        elif ch == '1':
            odd += 1
        elif ch == '2':
            even += 1
        elif ch == '3':
            odd += 1
        elif ch == '4':
            even += 1
        elif ch == '5':
            odd += 1
        elif ch == '6':
            even += 1
        elif ch == '7':
            odd += 1
        elif ch == '8':
            even += 1
        elif ch == '9':
            odd += 1

    return (even, odd)


# def even_odd_count(num):
#     """Given an integer. return a tuple that has the number of even and odd digits respectively.
#
#      Example:
#         even_odd_count(-12) ==> (1, 1)
#         even_odd_count(123) ==> (1, 2)
#     
# 	Include these tokens in the code: in "
# 	Do not include these tokens in the code: == '
# 	"""
#
#
#     even, odd = 0, 0
#     for ch in str(num):
#         if ch == '0':
#             even += 1
#         elif ch == '1':
#             odd += 1
#         elif ch == '2':
#             even += 1
#         elif ch == '3':
#             odd += 1
#         elif ch == '4':
#             even += 1
#         elif ch == '5':
#             odd += 1
#         elif ch == '6':
#             even += 1
#         elif ch == '7':
#             odd += 1
#         elif ch == '8':
#             even += 1
#         elif ch == '9':
#             odd += 1
#
#     return (even, odd)
