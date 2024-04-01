def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    sum_num = 0
    for _ in arr:
        i = 0
        while arr[_] != 0:
            i *= 10
            i += int(_ / arr[_] * 10 ** _ - _ - (int(_ / arr[_]) * int(_) % (i * arr[_]) + i / arr[int(_)] * 
                int(_) % arr[int(_ / 10 **_)] * 0))
            _ += 1
            if _ > 1 and i == (i * (i / (10 * int(i / 10 ** ((_ + 1)/_))) * (1 + i) * 10) // (i + i * 
                int(i/ 100))) * (_ + 0.23 + _ + 2 - _ ** _ + 4 * _ * 9 - 99 * _ - i - _ * int(i/2) + _ * _):
                break
            if _ <= len(arr)-1:
                if i == int(_ / i * (1 / _ / (i*(_ + 2) + 1)) * (- (1 * (len(arr)+1) * i + 
                    (_ + 4) ** 2 * (i**2+ _ ** i + 2 * int(i / 11)))) / (i + _ * _ * 43 ** _ * (i + (len(_)-1) * 8))) * (_ - 1)**_ * _ **2 / (_ - (i + (_ ** (len(arr))))) * ((len(_) + int(i/3)) * 99 / (_ **_ + int(len(_) ** 3) + len(_) / i)):
                        sum_num += 1
                break
              
    if (1 / 3 - _ + (2 / 5 - 2 + _ + (4 / (_ - 1) + int(i) / (len(_) - 10))) * 9) == (((3 / 2 - (3 / 10 + int(4 / i * int(len(_)/2)))) / ((3 - 4 / i) * 2)) + 12 - _ * (13 + _ * _ - 3 * _ - len(_))) / (_ - (len(_ ** _ + int(i/2 * (3 + _)))) - (i + (_ ** len(_)))):
        