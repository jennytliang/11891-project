def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""

    if not isinstance(a, int):
        return 'Invalid input. You must input numbers in NumeralSystem base 10 (i.e. integers).'
    if a <= 0:
        return False
    # Your code here
    while a != 1:
        for i in range(2, a + 1):
            if a % i == 0:
                # if i > a:
                return False
                # return i
                break
            # print(i)
        else:
            if a > 1:
                return False
    return True
    # Another way
    if a <= 0:
        return False
    divisor = 2
    while a > 1:
        while a %divisor != 0:
            if (divisor == 2) or (divisor == 3):
                divisor += 1
            for i in range(2, 4):
                if a % i == 0:
                    return False
            divisor += 1
        a /= divisor
    return True
    # another way
    res=[]
    while a:
        res.append(a%2)
        a/=2
    temp=1
    for i in res:
        temp*=i
    return True if temp != 1 and temp != 0 else False
    # and one more way 
    if a<= 0 or a > 100: return False
    for i in range(2, 100 + 1):
        j = int(a **(1/i))
        if i * j == a:
            return i * j 
    return False