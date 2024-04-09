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
    
	Do not include these tokens in the code: # R W Com bine the two
	"""
    # RW 02/03/2020
    vowels = "AEIOUaeiou"
    vowel = ""
    for i in range(len(word)-1,0,-1):
        if word[i] in vowels:
            vowel = word[i]
            break
    if vowel == "":
        return vowel
    for i in range(i,0,-1):
        if word[i] in vowels:
            return word[i]
    return ""

print(get_closest_vowel("yogurt")) # ==> "u"
print(get_closest_vowel("FULL")) # ==> "U"
print(get_closest_vowel("quick")) # ==> ""
print(get_closest_vowel("ab")) # ==> ""
