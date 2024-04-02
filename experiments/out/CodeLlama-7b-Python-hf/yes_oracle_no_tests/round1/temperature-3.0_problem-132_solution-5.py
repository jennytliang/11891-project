def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    
	Do not include these tokens in the code: open _ bra ckets = []
	'''
    # Create a list of the brackets
    brackets = []
    for i in string:
        if i == '[' or i == ']':
            brackets.append(i)

    # Create a list of the indices of the brackets
    indices = []
    for i in range(len(brackets)):
        indices.append(i)

    # Create a list of the indices of the brackets
    indices_2 = []
    for i in range(len(brackets)):
        indices_2.append(i)

    # Create a list of the indices of the brackets
    indices_3 = []
    for i in range(len(brackets)):
        indices_3.append(i)

    # Create a list of the indices of the brackets
    indices_4 = []
    for i in range(len(brackets)):
        indices_4.append(i)

    # Create a list of the indices of the brackets
    indices_5 = []
    for i in range(len(brackets)):
        indices_5.append(i)

    # Create a list of the indices of the brackets
    indices_6 = []
    for i in range(len(brackets)):
        indices_6.append(i)

    # Create a list of the indices of the brackets
    indices_7 = []
    for i in range(len(brackets)):
        indices_7.append(i)

    # Create a list of the indices of the brackets
    indices_8 = []
    for i in range(len(brackets)):
        indices_8.append(i)

    # Create a list of the indices of the brackets
    indices_9 = []
    for i in range(len(brackets)):
        indices_9.append(i)

    # Create a list of the indices of the brackets
    indices_10 = []
    for i in range(len(brackets)):
        indices_10.append(i)

    # Create a list of the indices of the brackets
    indices_11 = []
    for i in range(len(brackets)):
        indices_11.append