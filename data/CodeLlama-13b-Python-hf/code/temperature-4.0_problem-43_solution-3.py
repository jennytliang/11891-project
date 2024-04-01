def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # check if there are two distinct integers that sum up to zero and return True if yes

    # check if there is another instance of value + (-value) (in the list)

# Time: O(n^2), since, it goes n times, check for n+1 things
# Space: O(1), this is because it takes constant space, no matter how big is input
def isVowel(input):
    if input == 'a' or input == 'e' or input == 'i' or input == 'o' or input == 'u': 
       return True
    return False    

print(is_all_valid_spaces([1))
    

def is_valid_spaces_between_words(sentence):
    # check if all the space characters are between words 
    
    new_list = list(sentence.strip())
    
    # for index, ch in enumerate(list,start=):
test_str=""
