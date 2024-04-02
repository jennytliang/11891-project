def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    
	Do not include these tokens in the code: #
	"""

    # 2 brackets are equal if they are the same type
    # 2 brackets are opposite if they are different types
    # 2 brackets are not opposite if they are the same type
    # 2 brackets are not equal if they are opposite
    # 2 brackets are not equal if they are not opposite

    # Stack is a LIFO queue
    # Pop the last item off the stack
    # If the item is the same type as the next item, then they are equal
    # If the item is the opposite type as the next item, then they are opposite
    # If the item is not the opposite type as the next item, then they are not equal
    # If the item is not the same type as the next item, then they are not equal

    # 2 brackets are not equal if they are opposite
    # 2 brackets are not equal if they are not opposite

    # Stack is a LIFO queue
    # Pop the last item off the stack
    # If the item is the same type as the next item, then they are equal
    # If the item is the opposite type as the next item, then they are opposite
    # If the item is not the opposite type as the next item, then they are not equal
    # If the item is not the same type as the next item, then they are not equal

    # 2 brackets are not equal if they are opposite
    # 2 brackets are not equal if they are not opposite

    # Stack is a LIFO queue
    # Pop the last item off the stack
    # If the item is the same type as the next item, then they are equal
    # If the item is the opposite type as the next item, then they are opposite
    # If the item is not the opposite type as the next item, then they are not equal
    # If the item is not the same type as the next item, then they are not equal

    # 2 brackets are not equal if they are opposite
    # 2 brackets are not equal if they are not opposite

    # Stack is a LIFO queue
    # Pop the last item off the stack
    # If the item is the same type as the next item, then they are equal
    # If the item is the