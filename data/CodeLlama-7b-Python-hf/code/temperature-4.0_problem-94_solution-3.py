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
    """

    s = set()
    prime = [i for i in lst if i > 1]
    r = [x for x in prime if x <= prime[len(prime) - 1]]
    l = set()
    for v in r:  # i is here a list
        for x in r:
            for n in r:
                    if (x % x) < 1 == (v % x):
                        print(v, x)
            a = v + x

            ln = a / 2 if (v <= lst) and (x < lst) else 2 / v if (lst / v == 2 % x) and (x * x) == 0 else 1 + v if v > lst else 0

            if n not in l and v == x * ln < x or x != x:
                if x == prime[0] or x > 0:    # s.add(x)    if x <= prime[0] and x > lst:  # for x in prime [0]
                    l.add(x)                     # if x> v and x < x*x:
            lst = lst * x if x < lst:
    return(sum(x + lst, ln))
# 81 + 25 + 1 + 3 + 3 + 1 + 1 +
