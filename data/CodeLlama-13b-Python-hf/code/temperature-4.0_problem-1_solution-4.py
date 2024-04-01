from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # if paren_string[0] != ")" or paren_string[-2] != "(": return False
    str_index, group_start, temp_dict, output = 0, 0, {}, []
    
    
    for index, string in enumerate(paren_string):
        # if opening parentheses, add the index in a dictionary
        if paren_string[index] == "(":
            group_start = index
            # if it already contains key, check if it's empty. if is, replace. else, append. if the value is already present, check the key and update the key if necessary.
            if str(index) not in temp_dict.keys():
                empty = True if len(list(temp_dict.values())[-1]) == 0 else False
                if not empty: #if the last index has length
                    temp_dict[str(index)] = string
            # check if it already contains values or keys (if not, then if not empty is already false, which means the value is replaced.)
            # otherwise, find the last value in the dict. if length is equal to 1, if the current string is ")", it is removed from temp_dict, else it should be changed to empty array. 
            # if index already exists, the dictionary should append to it. if not, add the key.
            else:
                if (len(list(temp_dict[list(temp_dict.keys())[-1]])[0]) == 1 and (string == ")" )):
                    # if this is true and the string is a closing paranthesis and it is empty, it is deleted, otherwise the previous key should be appended
                    empty_dict = True if (list(temp_dict.values()))[-1].pop() == [] else False
                    if (not bool(empty_dict)):
                        prev = (list(temp_dict.keys()))[-2]
                        # if prev exists, then just append to that key
                        if prev in (temp_dict).keys():
                            temp_dict[prev].append([list(temp_dict[str(prev)])[0] + [list()]])
                        # otherwise, since we are using string and not indexs, the prev is not in dict, so, we know that key is not defined, so we should directly append the value in prev. append this value: [str(prev) + [list()]]) to group_start (key value is 
                        # actually the key's index value. since we use "str" and not indexes, the string value can be mapped with the index in the string when the time comes to check the indexs.

        
        # if closing parenthesis exists and has not yet been added in temp_dict, then add it in empty dictionary
        # check if the string value has been appended as in the example in previous comment
        if paren_string[index].isalpha() == False:
            print(temp_dict, "dictionary after adding closing parenthesis(if it was appended")
        
        
        # if non-bracket string character is identified, append the value to the key-values and then pop the dict


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()  
    # input()