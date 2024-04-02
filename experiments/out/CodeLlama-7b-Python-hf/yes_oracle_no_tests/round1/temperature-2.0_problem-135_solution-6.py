def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: for i in range ( len ( arr ) -
	"""
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return i

    return -1


# 🚨 Do NOT change any of the code below 
import time


def main():
    start = time.time()
    array = [int(x) for x in input('Enter the array: ').split()]
    result = can_arrange(array)
    end = time.time()
    print(f'{result} is the largest index of an element which is not greater than or equal to the element immediately preceding it.')
    print(f'Execution time: {end - start} seconds')


if __name__ == '__main__':
    main()

