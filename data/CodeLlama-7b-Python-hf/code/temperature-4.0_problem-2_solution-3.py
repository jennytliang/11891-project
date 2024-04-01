def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if number >=1:
        integer, float_part = int(number), number - int(number)
        # add one to the nearest integer part to calculate the decimal parts
        decimal_parts = float_part-int(number)
        print((int(number)))
    return decimal_parts


if __name__ == '__main__':
    number = float(input("Enter your number here:"))