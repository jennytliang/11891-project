def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    return is_palindrome_left_right_caret(text)
    # Another solution using slicing (which is very similar to the one above and can be adapted to the other solution)
    text_reverse = text[::-1]
    return text == text_reverse

def is_odd_length(text):
    return len(text) % 2 != 0

def middle_char_index(string, is_odd=False):
    middle_char = (len(string) if is_odd else len(string))//2
    middle = string[middle_char]         # 
    return middle_char
    

def is_palindrome_left_right_caret(text):
    is_odd_text = is_odd_length(text)        # 
    middle = middle_char_index(text)            # returns index 2 for ababa
    #print(text)
    #print(middle)
     #   [0:middle]     [2:]
    #    [0:1,0:1,1,1],[1:2,2:1]         # [0:middle]
    #       [A,A],   [A] 
    if text[middle] != text[-middle-1]:      # text[2:1] - empty -> 
        return False            # if it's not the very middle letter return false, otherwise it is
    left, right = text[0:middle], text[middle:]      #  AB  /  
    if left[::-1] == right or (left[1::] == right and left[0] == text[-1]):      # BA   |   ABA      [0:-1], [-1:1:-1] 
        return True 
    return 


