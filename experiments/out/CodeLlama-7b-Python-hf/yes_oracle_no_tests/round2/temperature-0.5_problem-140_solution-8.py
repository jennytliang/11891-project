def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ), 2 , - 1 ):
	Do not include these tokens in the code: )):
	"""


    ans = text
    for i in range(le):
        if ans[i] == ' ':
            ans = ans.replace(ans[i], '_')
    return ans




def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ), 2 , - 1 ):
	Do not include these tokens in the code: )):
	"""

    ans = ''
    for i in range(le):
        if text[i] == ' ':
            if ans[-1] == ' ':
                ans += '-'
            else:
                ans += '_'
        else:
            ans += text[i]
    return ans



# def fix_spaces(text):
#     """
#     Given a string text, replace all spaces in it with underscores, 
#     and if a string has more than 2 consecutive spaces, 
#     then replace all consecutive spaces with - 
    
#     fix_spaces("Example") == "Example"
#     fix_spaces("Example 1") == "Example_1"
#     fix_spaces(" Example 2") == "_Example_2"
#     fix_spaces(" Example   3") == "_Example-3"
    
#     Include these tokens in the code: ), 2 , - 1 ):
#     Do not include these tokens in the code: )):
#     """

#     ans = ''
#     for i in range(len(text)):
#         if text[i] == ' ':
#             if ans[-1] == ' ':
#                 ans += '-'
#             else:
#                 ans += '_'
#         else:
#             ans += text[i]
