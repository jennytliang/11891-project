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
    # R2:
    # if word == "":
    #     return ""
    # if word.isalpha() == False:
    #     return ""
    # if word.isupper():
    #     word = word.lower()
    # if word[0] in 'aeiou':
    #     return ""
    # if word[-1] in 'aeiou':
    #     return ""
    # for i in range(len(word)-1, 0, -1):
    #     if word[i].isalpha() == False:
    #         continue
    #     if is_vowel(word[i]) == True:
    #         return word[i]
    # return ""

    # R1:
    if word == "":
        return ""
    if word.isalpha() == False:
        return ""
    if word.isupper():
        word = word.lower()
    for i in range(len(word)-1, 0, -1):
        if word[i].isalpha() == False:
            continue
        if is_vowel(word[i]) == True:
            return word[i]
    return ""

def is_vowel(ch):
    if ch.lower() in 'aeiou':
        return True
    else:
        return False


if __name__ == '__main__':
    print(get_closest_vowel("yogurt")) # "u"
    print(get_closest_vowel("FULL")) # "U"
    print(get_closest_vowel("quick")) # ""
    print(get_closest_vowel("ab")) # ""
    print(get_closest_vowel("abc")) # ""
    print(get_closest_vowel("abcde")) # ""
    print(get_closest_vowel("abcdef")) # ""
    print(get_closest_vowel("abcdefg")) # ""
    print(get_closest_vowel("abcdefghijklmnopqrstuvwxyz")) # ""
    print(get_closest