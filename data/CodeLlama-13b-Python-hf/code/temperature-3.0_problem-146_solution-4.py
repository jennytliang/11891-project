def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    cnt = 0
    for n in nums:
        lastDigit = int(str(n)[-1])
        firstDigit = int(str(n)[0])
        if n > 10 and lastDigit % 2 and firstDigit % 2:
            cnt += 1
    return cnt

print(specialFilter([15, -73, 14, -15]))