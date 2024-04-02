def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: if len ( s ) ==
	"""
    
    print("s = " + s)
    
    if s == '': # base case
        return []
    
    # recursive case
    first_space_index = s.find(' ')
    if first_space_index == -1:  # first space_index
        return []
    print("first_space_index is " + str(first_space_index))
    
    first_word = s[:first_space_index]
    print("first_word is " + first_word)
    
    result = select_words(s[first_space_index + 1:], n)
    if result == []:
        return result
        
    if len([c for c in first_word if c not in 'aeiou']) == n:
        answer_list = [first_word] + result
        return answer_list
    return result


s = "Mary had a little lamb"
n = 4
print('[s, n] = [\"' + s + '\", ' + str(n) + ']')
print(select_words(s, n))
print('==================================================================')

s = "Mary had a little lamb"
n = 3
print('[s, n] = [\"' + s + '\", ' + str(n) + ']')
print(select_words(s, n))
print('==================================================================')

s = ""
n = 2
print('[s, n] = [\"' + s + '\", ' + str(n) + ']')
print(select_words(s, n))


    
