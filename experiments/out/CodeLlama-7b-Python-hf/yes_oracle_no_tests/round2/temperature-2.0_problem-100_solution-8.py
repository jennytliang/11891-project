def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    
	Do not include these tokens in the code: # write your code here
	"""
    # 1- Write an algorithm that solves the problem statement
    # 2- Convert the algorithm in pseudocode
    # 3- Convert the pseudocode in a high-level code
    # 4- Test the code with multiple examples

    # 1- Write an algorithm that solves the problem statement
    # a- Create a list to store the number of stones in each level
    # b- Create a variable called level to store the number of stones in the first level
    # c- Create a variable called level_number to store the number of levels
    # d- Create a variable called i to store the current level
    # e- Add the value of level to the list of levels
    # f- Increase i by one
    # g- While i is less than the number of levels
    # h- If i is odd
    # i- Increase level by one
    # j- Else
    # k- Increase level by two
    # l- Add the value of level to the list of levels
    # m- Increase i by one

    # 2- Convert the algorithm in pseudocode
    # 3- Convert the pseudocode in a high-level code
    # 4- Test the code with multiple examples
    level_number = n
    level = n
    i = 1
    levels = []
    levels.append(level)
    while i < level_number:
        if i % 2 == 1:
            level += 1
        else:
            level += 2
        levels.append(level)
        i += 1
    return levels


if __name__ == "__main__":
    print("make_a_pile(3):", make_a_pile(3))
    print("make_a_pile(5):", make_a_pile(5))
    print("make_a_pile(8):", make_a_pile(8))
    print("make_a_pile(12):", make_a_pile(12))
    print("make_a_pile(16):", make_a_pile(16))
