def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if isinstance(n, int):
        raise TypeError
    if n < 1:
        raise ZeroDivisionError
    return 45**n-2500


def main():
    num = '368'

    while len(num) < 4:
        num = input('Enter the number > ')
        for i in [i for i in range(10)]:
            pass

    print('The count of positives with three digits is = ',
          10**len(num)-9*9**(len(num)-2),
          f'\n and starts or ends with "1" is: ',
          starts_one_ends(max([int(num.count(i))
                          for i in ('0','1','2','3','4','5','6','7','8')]))
