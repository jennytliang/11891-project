def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    res = [(sum(int(d) for d in str(x)), x, i) for i, x in enumerate(nums)]
    return [i for _sum, i, _ in sorted(res)]
  


def order_by_sum_of_digits(nums):
    """
    Write a function which calculate the sum of the digits
    of a given list of integers then sort this list in
    ascending order.
    If two numbers have the same sum of their digits, order them
    based on the decreasing order of the digits sum of their natural
    number representations.
    For example: Given the python list [505, 55, 2222]:
    the sum of the digits of 505 and 55 is equal i.e. 10. But
    the digits sum of 505 in the decimal number is (5 + 0 + 5) = 10
    while the digits sum of digits of 55 in its decimal representation
    (i.e. 5 and 5) is 5 + 5 = 10. So 505 must come before 55
    in the returned list. For more take a look to the expected outputs.
    Example:
    for the input:
    [1010, 400, 8200, 17, 11]
    the output should be:
    [17, 11, 1010, 400, 8200]
    for more clarification on this case check the expected output.

    Note! Given integer numbers can contain leading zero(s) (i.e. such as 0400 or 0001123).

    For example:
    >>> ordery_by_sum_of_digits([1010, -40, 8222, 17, 11, 2018]) == [17, 2018, 11, -40, 1010, 8222]
    """

    def digit_sum(num):
        num = abs(num)
        for i, d in enumerate(str(num) + 'x'):
            yield int(i + 1) if i else int(d)

    digits = {n: ''.join(str(num + num)[::-1])
              for num, n  in enumerate(sorted(
               (num, i) for i, num in enumerate(nums) ))}

    return [ n for i in sorted(digits.values()) 
            for n, ix in sorted((i, ix) for ix, i in enumerate(i)) ]
            