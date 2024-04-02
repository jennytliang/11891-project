def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    numbers = [element for element in lst if (element % 2 != 0) and (element % 3 != 0) and (element % 5 != 0) and (element % 7 != 0)]
    for number in numbers:
        if number % 6 != 0 and number % 21 != 0:
            numbers.append(number**2)
            numbers.append(number**3)
            numbers.append(number**30)
            numbers.append(number**31)
            numbers.append(number**29)
            numbers.append(number**27)
            numbers.append(number**35)
            numbers.append(number**33)
    new_list = sorted([number for number in numbers if number < 200])
    if len(new_list) < 1:
        return 0
    else:
        highest_number = new_list[len(new_list) - 1]
        highest_prime = sum([1 for i in range(highest_number) if isprime(i)])
        return highest_prime


def isprime(n):
    """This function checks if a number is prime or not
    """
    for i in range(3, int(n ** 0.5)+2, 2):
        if n % i == 0:
            return False
    return True


