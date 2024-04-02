def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    
	Do not include these tokens in the code: if not string : return
	'''
    # 1st solution
    # if len(string) == 0:
    #     return False
    # elif len(string) == 2:
    #     return string == '[]'
    # else:
    #     return string[1] == ']' and string[0] == '[' and is_nested(string[2:-1])

    # 2nd solution
    return ']' in string and '[' in string and is_nested(string.replace(']', '').replace('[', ''))


# print(is_nested('[[]]'))
# print(is_nested('[]]]]]]][[[[[]'))
# print(is_nested('[][]'))
# print(is_nested('[]'))
# print(is_nested('[[][]]'))
# print(is_nested('[[]][['))


def check_sentence(sentence):
    '''
    Create a function that takes a sentence and returns True if the sentence 
    contains only alphabetical words, and False otherwise.
    A word is a sequence of letters optionally separated by non-letter characters.

    check_sentence('Hello world') ➞ True
    check_sentence('Hello world!') ➞ False
    check_sentence('Hello9world') ➞ False
    check_sentence('') ➞ True
    
	Do not include these tokens in the code: if not sentence : return
    '''
    # 1st solution
    # if len(sentence) == 0:
    #     return True
    # else:
    #     return sentence[0].isalpha() and check_sentence(sentence[1:])

    # 2nd solution
    return all(x.isalpha() for x in sentence.split())


print(check_sentence('Hello world'))
print(check_sentence('Hello world!'))
print(check_sentence('Hello9world'))
print(check_sentence(''))


def is_valid(brackets):
    '''
    Create a function that takes a string and returns True if the string 