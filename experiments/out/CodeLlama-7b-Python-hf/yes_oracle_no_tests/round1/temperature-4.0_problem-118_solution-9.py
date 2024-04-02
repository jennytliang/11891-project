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
    # Rely on the built-in function.
    return min(filter(lambda x: x != '', map(lambda x: x[0], filter(lambda x: x[1] > 0,
        enumerate(map(lambda x: x.isvowel(), reversed(word)))))))

    # My own solution.
    # import re
    # if re.search(r'[^aeiou]?([aeiou])[^aeiou]', word) is None:
    #     return ''
    # else:
    #     return re.search(r'[^aeiou]?([aeiou])[^aeiou]', word).group(1)

    # My own solution.
    # vowels = 'aeiou'
    # for i in range(len(word)):
    #     if word[i] in vowels:
    #         if i < len(word) - 1:
    #             if word[i + 1] in vowels:
    #                 return word[i]
    #         if i > 0:
    #             if word[i - 1] in vowels:
    #                 return word[i]
    # return ''

    # My own solution.
    # if len(word) < 2:
    #     return ''
    # if word[-1] in 'aeiou':
    #     return ''
    # if word[-2] in 'aeiou':
    #     return ''
    # return min([x for x in word[-2:] if x in 'aeiou'])

    # My own solution.
    # if len(word) < 2:
    #     return ''
    # if word[-1] in 'aeiou':
    #     return ''
    # if word[-2] in 'aeiou':
    #     return ''
    # return min([x for x in word[-2:] if x in 'aeiou'])

    # My own solution.
    # if len(word) < 2:
    #     return ''
    # if word[-1] in 'aeiou