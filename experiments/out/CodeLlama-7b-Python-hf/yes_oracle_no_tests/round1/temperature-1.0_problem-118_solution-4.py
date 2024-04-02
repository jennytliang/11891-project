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
    # Rough code
    if len(word) == 1:
        return ""
    elif len(word) == 2:
        if is_vowel(word[0]) and is_vowel(word[1]):
            return ""
        elif is_vowel(word[0]) and not is_vowel(word[1]):
            return word[0]
        elif not is_vowel(word[0]) and is_vowel(word[1]):
            return word[1]
        else:
            return ""
    else:
        last = word[-1]
        second_last = word[-2]
        if is_vowel(last) and is_vowel(second_last):
            return ""
        elif is_vowel(last) and not is_vowel(second_last):
            return last
        elif not is_vowel(last) and is_vowel(second_last):
            return second_last
        else:
            return ""
        

def is_vowel(ch):
    if ch in "aeiou":
        return True
    else:
        return False

print(get_closest_vowel("yogurt")) # "u"
print(get_closest_vowel("FULL")) # "U"
print(get_closest_vowel("quick")) # ""
print(get_closest_vowel("ab")) # ""