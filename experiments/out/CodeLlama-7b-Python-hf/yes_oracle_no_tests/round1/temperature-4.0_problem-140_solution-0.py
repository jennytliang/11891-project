def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ans =
	Do not include these tokens in the code: res =""
	"""
    #TODO: Write your code below this line
    res = ""
    for char in text:
        if char == " ":
            res += "_"
        else:
            res += char
    ans = res
    #TODO: Write your code above this line
    return ans

if __name__ == '__main__':
    with open('example.txt', 'r') as example_txt:
        with open('output.txt', 'w') as output_txt:
            for line in example_txt:
                output_txt.write(fix_spaces(line))