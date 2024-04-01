from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """


def main():
    print("Check if two rectangles have a common side:")
    width_1 = int(input("Width of the first rectangle: "))
    height_1 = int(input("Height of the first rectangle: "))
    width_2 = int(input("Width of the second rectangle: "))
    height_2 = int(input("Height of the second rectangle: "))

    print(common_side(width_1, height_1, width_2, height_2))


if __name__ == "__main__":
    main()
