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
    # Rough Code
    # 1. check if word is empty
    # 2. check if the first and last char are vowels
    # 3. loop through the word from right to left
    #    if the current char is a vowel, check if the previous char is a consonant
    #      if so, return the current char
    # 4. return empty string

    if len(word) == 0:
        return ''

    if word[0] in 'AEIOUaeiou':
        if word[0] in 'aeiouAEIOU':
            word = word[1:]
        if len(word) == 0:
            return ''

    if word[-1] in 'AEIOUaeiou':
        if word[-1] in 'aeiouAEIOU':
            word = word[:-1]
        if len(word) == 0:
            return ''

    for i in range(len(word) - 2, -1, -1):
        if word[i] in 'AEIOUaeiou':
            if word[i] in 'aeiouAEIOU':
                word = word[:i+1]
            if len(word) <= 1:
                return ''

            if word[i-1] in 'AEIOUaeiou':
                if word[i-1] in 'aeiouAEIOU':
                    word = word[:i]
                return word[i]

    return ''

    # TODO: Refactor the rough code above



print(get_closest_vowel("yogurt")) # 'u'
print(get_closest_vowel("FULL")) # 'U'
print(get_closest_vowel("quick")) # ''
print(get_closest_vowel("ab")) # ''
print(get_closest_vowel("abc")) # ''
print(get_closest_vowel("abcY")) # 'Y'
print(get_closest_vowel("aYbc")) # 'Y'
print(get_closest_vowel