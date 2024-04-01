def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    if n==0:
        return 0
    
    total=1
    for i in str(n):
        num=int(i)
        if num%2==1:
            total*=num
    return total


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digits(1) == 1, "1st example"
    assert digits(4) == 0, "2nd example"
    assert digits(115) == 75, "3rd example"