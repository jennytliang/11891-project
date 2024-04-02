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

    #TODO: Write your code below this line
    #pass

    stack = []
    for char in brackets:
        if char == '<':
            stack.append(char)
        elif char == '>':
            if stack:
                stack.pop()
            else:
                return False
    return not stack


#submit correct_bracketing


# 2.3

def longest_increasing_subsequence(numbers):
    """Return the longest subsequence of numbers that are increasing
    (i.e. subsequence[i] <= subsequence[i+1])
    >>> longest_increasing_subsequence([3, 4, -1, 5, 8, -6])
    [3, 4, 5, 8]
    >>> longest_increasing_subsequence([10, 1, 2, 3, 4])
    [10, 1, 2, 3, 4]
    >>> longest_increasing_subsequence([])
    []
    >>> longest_increasing_subsequence([1])
    [1]
    """
    #TODO: Write your code below this line
    #pass
    subsequence = []
    max_subsequence = []
    for num in numbers:
        if not subsequence or num <= subsequence[-1]:
            subsequence.append(num)
        else:
            while subsequence and num > subsequence[-1]:
                subsequence.pop()
            subsequence.append(num)
        if len(subsequence) > len(max_subsequence):
            max_subsequence = subsequence[:]
    return max_subsequence


#submit longest_increasing_subsequence
