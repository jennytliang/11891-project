def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    
	Include these tokens in the code: def is
	Do not include these tokens in the code: pass has
	"""
    vowels = ['A', 'E', 'I', 'O', 'U']
    # print('vowels: ', vowels)
    word_list = list(word.upper())
    print(word_list)
    right_str = ''
    for ch in word_list[::-1]:
        if ch not in vowels:
            right_str = ch + right_str
        else:
            break
    
    left_str =''
    for ch in word_list:
        if ch not in vowels:
            left_str = left_str + ch
        else:
            break
    
    if right_str == '' or left_str == '':
        return ''
    
    if (right_str[2:] == left_str[1:-1]) or (right_str[1:-1] == left_str[2:]):
        return word[1:-1]
    else:
        return right_str + left_str
            

print(get_closest_vowel("yogurt") == 'u')
print(get_closest_vowel("cash"))
