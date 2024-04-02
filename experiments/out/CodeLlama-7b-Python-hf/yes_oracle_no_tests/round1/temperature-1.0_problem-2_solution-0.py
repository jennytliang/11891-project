def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return number - int(numb)

if __name__ == '__main__':
    for number in range(1, 100):
        # If the number can be divided by 10 without leaving a remainder
        if number % 10 == 0:
            # End the loop
            break
        number = float(input("Enter a positive number: "))
        print(number, "is composed of:")
        print(f"Integer part = {truncate(number)}")
        print(f"Decimal part = {truncate(number):.1f}")