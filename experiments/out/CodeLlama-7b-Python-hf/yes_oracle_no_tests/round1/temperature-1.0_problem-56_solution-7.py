def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    
	Include these tokens in the code: c nt =
	"""
    return count_chars(brackets, "]", False) == count_chars(brackets, "[", True)



def balance_pizza(customers):
    """ 
    Take a sequence of numbers of customers, which we represent in python as a list.
    Your function should return the number of customers that would be satisfied with at least a little pizza. 
    That is, return how many would be happy if we gave them pizza, but we don't have to give them exactly our best pizza,
    we can give any amount larger than 14, or 9 / 14 of our best pizza.

    >>> balance_pizza([15, 16, 15, 14, 16, 17])
    3
    >>> balance_pizza([16, 18])
    1
    >>> balance_pizza([16, 16])
    2
    >>> balance_pizza([18, 22])
    1
    >>> balance_pizza([5, 5, 3, 5, 5, 8, 5, 10, 5, 6])
    7
    
    >>> balance_pizza([5, 5, 3, 5, 5, 17, 5, 10, 5, 6])
    5
    
    INPUT:
    customers; a list(int) of the number of customers that asked for a pizza 
    
    OUTPUT; int
    the amount of customers who would get a pizza
    
    EXAMPLES:
    4 total customers, 2 getting pizza.
    [14,14,1,14] -> 3
    [13, 13, 13] -> 3
    4 total customers, 1 getting pizza.
    [14,14,1,7] -> 3
    """
    slices_needed = []
    for pizza_type in customers:
        if pizza_type >= 14 or pizza_type >= 9 / 14 * 14: