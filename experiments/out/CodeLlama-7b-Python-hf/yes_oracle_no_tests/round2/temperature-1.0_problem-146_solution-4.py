def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: ans , odd =
	"""
    odd = set([1, 3, 5, 7, 9])
    ans = 0
    for num in nums:
        num = abs(num)
        if len(str(num)) < 2:
            break
        if num > 10:
            strNum = str(num)
            if int(strNum[0]) in odd and int(strNum[-1]) in odd:
                ans += 1
    return ans


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
if __name__ == '__main__':
    array = input('Enter numbers: ').strip().split(' ')
    nums = [int(num) for num in array]
    print(specialFilter(nums))
