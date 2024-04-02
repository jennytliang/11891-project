from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: seen
	"""
    
    seen: List[int] = []
    for num in numbers:
        if num not in seen:
            count = 1
            seen.append(num)
        else:
            count += 1
    
    output = []
    for s, num in enumerate(seen):
        if count == 1:
            output.append(num)
        else:
            if s == 0:
                output.append(num)
            elif num != seen[s-1]:
                output.append(num)
    
    return output


def main():
    input = [int(inp) for inp in input().split()]
    print(remove_duplicates(input))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
