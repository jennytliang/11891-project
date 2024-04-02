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
    
	Include these tokens in the code: def is _ v owel ( ch : str )
	"""
    word = word.upper()
    if len(word) < 3:
        return ''
    
    for k in range(len(word)-2, 0, -1):
    	if is_vowel(word[k]) and not is_vowel(word[k+2]):
    		return word[k+1]
    
    return ''
    

def is_vowel(char):
    return char in ['A', 'E', 'I', 'O', 'U', 'y'] or char[-1] == 'Y'

    
                    
def main():
    a = get_closest_vowel("yogurt")      # a == "u"
    print(a)
    
    b = get_closest_vowel("FULL")       # b == "U"
    print(b)
    
    c = get_closest_vowel("quick")      # c == ""
    print(c)
    
    d = get_closest_vowel("ab")         # d == ""
    print(d)
    
    e = get_closest_vowel("uabcu")      # e == "a"
    print(e)
    
    f = get_closest_vowel("uabcuz")      # e == "a"
    print(f)


if __name__ == '__main__':
    main()
