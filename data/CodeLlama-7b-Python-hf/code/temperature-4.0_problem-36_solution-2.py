def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    nums = [n//131, n//55, n]

    answer = 0
    for num in nums: 
        while num>0:
             if num%10 ==7: # 7 appears
                num=num//10 # cut it out of number, the first digit
                if num%131 == 0: # divisible by 55, (7*13) is divisible by  11 (5*7*7 or 5*29, 29 = 21*11-18, 21=5^2 13, 73, 67, 79, 901, 561) 
                 answer = answer+1 # answer +=1 when the digits appears and when the dividble by divisible 
 
             else:
                num=0 # exit the while
    return answer