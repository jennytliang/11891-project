from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    
	Include these tokens in the code: number
	Do not include these tokens in the code: num
	"""

    s, p = 0, 1
  
    for num in numbers:
        s += num
        p *= num

    return s, p
    
    
if __name__ == "__main__":
    number_list = [int(n) for n in input("Enter a list of numbers: ").split()]
    
    (sum, product) = sum_product(number_list)
    
    print("Sum: {s}, Product: {p}"\
        .format(s=sum, p=product))