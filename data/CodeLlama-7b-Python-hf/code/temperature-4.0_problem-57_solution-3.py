def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # sort list into ascending order, then iterate from both ends
    s_list = sorted(int(element) for element in l)
    # check for equality of the first consecutive elements, then iterate from second consecutive
    for pos in range(len(l)-1):
        if l[pos] == s_list[pos] and l[pos+1] == s_list[pos+1]:
            continue
        # compare the values between consecutive elements starting from pos + 1
        # and l - 1.
        for start, finish, index in [(pos, len(l), 0),
                             (-len(l), -1, -1)]:# iterating through a range, starting at the neg. of the range
            # increment through values, starting with start, finish at pos + 1, decrementing until the range
            for index in range(start, finish, index ):
                # if a value is less than the following element, return false. Then check for equality, and
                # then check for the 2nd next elements. If they do not equal, restart the comparisons with
                # the following elements until the two do equal, then return False. Then restart the checks.
                # if they continue to be less, return the False. Otherwise, proceed with the final step and return
                # the final value to be true if they are both equal. If they go through the list with each step, and
                # all the values compare equal, then they return true.

                    if l[index] <= s_list[index + 1] and s_list[index+1] == l[index + 1]:
                        continue
                    elif l[index] <= s_list[index + 1] and not s_list == l:
                        if l[index] + 1 != s_list[pos+2]:#l[index+pos + 1] ==l[index] and l[index + 1] == s_list[index+1]
                            return True
                        elif l[index] == 1 == s_list[pos+2]:
                            index += 1 # or else just continue
                        # and then the next value or else,
                    if index == len(l) - 4: # when we are all done, we simply return True if it has made it to the last index and the list is sorted in order of equality
                        return True #if we did not break, otherwise return False

                elif start == finish and l[index] <= l[pos +1]: # if the list has finished and the elements don't equal
                # then we can exit, otherwise, iterate through the list, adding 1
