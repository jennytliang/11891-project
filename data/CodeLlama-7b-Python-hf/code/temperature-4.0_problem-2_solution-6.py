def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    decimals = abs(num % 1)
    
    
    return float(decimals) 
    
num = 35.75
print("Decimal part of the float number is: " + str(truncATE_Nuber(num2)))
