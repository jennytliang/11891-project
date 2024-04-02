def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge ( x : int ) -> int :
	"""
    sum_nums = []
    for num in arr:
        if num < 0:
            num = num * -1
        sum_num = 0
        while num > 0:
            sum_num += num % 10
            num = num // 10
        sum_nums.append(sum_num)
    return sum_nums.count(sum_nums)


# def test_function(test_case):
#     arr = test_case[0]
#     solution = test_case[1]
#     output = count_nums(arr)
#     if output == solution:
#         print("Pass")
#     else:
#         print("Fail")


# # test_case_1 = [[], 0]
# # test_function(test_case_1)

# test_case_2 = [[-1, 11, -11], 1]
# test_function(test_case_2)

# test_case_3 = [[1, 1, 2], 3]
# test_function(test_case_3)

# test_case_4 = [[123, 321], 2]
# test_function(test_case_4)

# test_case_5 = [[-456, -654, 789], 0]
# test_function(test_case_5)

test_case_6 = [[123, -456, 789], 2]
test_function(test_case_6)



# print(count_nums([1, 1, 2, 99, 9]))
# print(count_nums([1, 1, 2, -99, 9]))
# print(count_nums([1, 1, 2, -99, -9]))
# print(count_nums([1, 1, 2, 99, -9]))
# print(count_nums([1, 1, 2, 999, -9