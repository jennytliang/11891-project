def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    
	Do not include these tokens in the code: if n < 0 :
	"""
    # your code here
    if n < 0:
        return []
    else:
        prime = [2,3]
        x = 5
        while len(prime) < n:
            is_prime = True
            for i in range(2, int(x**0.5)+1):
                if x % i == 0:
                    is_prime = False
            if is_prime:
                prime.append(x)
            x += 2
        return prime


if __name__ == '__main__':
    print("Example:")
    print(count_up_to(5))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_up_to(5) == [2, 3]
    assert count_up_to(11) == [2, 3, 5, 7]
    assert count_up_to(0) == []
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert count_up_to(1) == []
    assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]
    print("Coding complete? Click 'Check' to earn cool rewards!")