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
    lst  = word
    lst =[t for t in lst if t not in "aAeiEoOuU"]

    
    vwl = []
    for c in lst:
        if c is 'a' or c is 'e' or c is 'i' or c is 'o' or c is 'u':
            vwl.append(c)
    s=vwl[0:][-2:]
    print(s)
    
    
    pass

print(get_closest_vowel("yogurt"))
