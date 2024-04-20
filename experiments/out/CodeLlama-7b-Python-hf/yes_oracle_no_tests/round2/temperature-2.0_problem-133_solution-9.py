def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    
	Include these tokens in the code: import math
	Do not include these tokens in the code: # # This is the solution I
	"""
    # # Your code here
    sum_squares = 0
    for i in lst:
        i = math.ceil(i)
        sum_squares += i ** 2
    return sum_squares


if __name__ == '__main__':
    with open('./data.txt', 'r') as f:
        test_cases = f.readlines()
        for test in test_cases:
            lst = [int(i) for i in test.split()]
            result = sum_squares(lst)
            print(lst, result)