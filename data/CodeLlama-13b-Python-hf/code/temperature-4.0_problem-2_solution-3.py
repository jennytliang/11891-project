def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


def get_truncated_number_length(length_decimal_part: float) -> float:
    """ Return a floating number which is the length of the number we are removing
    from passed in floating number's length(decimal part) by removing 0 at it's begining. (e.g 0.032 will become 0.32 after)

    1.0234 will be also 1.0234 because it's longer than 1 (so length is already 5 characters so remove 0 from the beginning)
    so length of this number is still 5. So number is 1, length of number is 5

    0004351  will become 4351 because length of the decimal part should be less than the number. Hence the 0 at the begining of it should be removed

    length should be <= number, that's why if length is == number, remove one leading zero
    >>> get_truncated_number_length(1234)
    434
    length is smaller than number, then just use this as length

    number is smaller and length, then it's already in decimal part so it is already removed first 0 from the number
    number is smaller than length but length has trailing 0 in first decimal position. If that's first 0 then remove first 0 (e.g 6005.0451, length: 6, length is bigger by 5 then number, but first 0, so remove first 0. Then 505.4451) So
    length can already be bigger than number, 5 is bigger than 4.0 but not bigger than 451.00. So you should make it smaller to make it work. If 505,1456, then keep 4, because it's smaller and not bigger than it's number 5. 5 is also 5 because 5 starts with number 5 and last two decimals start with 4, 5,6 so 5, and 6 is already greater then 4.55 because 55>455. 4 should be also there, because 4 is also after 5, and it's bigger than 3 (if you do 3)

    If length is bigger > number, number is smaller than 1 remove 1


    # length can be bigger for example 5856531.0413, it's length will 9 and it's number is smaller than 5 so just make it less by 1
    length >= 5 then return: number - 0.000
    0 should also be there
    and it can't get bigger because length is bigger then number, if bigger then use length of number and put 0 in between.

    Examples
    >>>  get_truncated_numbers_length(1234.00) # number is bigger and 2345.0 is not possible, because number is smaller then 1 and 0. because 04 is also possible (because if you put more decimals then it should be the same then original number) but the original is same as 00 so put 1 instead
    >>> 1.0435
    10.532210456863947
    5.5555
    1.2223451757116064e-15
"""