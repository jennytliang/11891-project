def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
	Include these tokens in the code: return
	Do not include these tokens in the code: if number >= 1 :
	"""
    return number - int(number)


def main():
    number = float(input("Enter a positive floating point number: "))
    print(truncate_number(number))


if __name__ == "__main__":
    main()