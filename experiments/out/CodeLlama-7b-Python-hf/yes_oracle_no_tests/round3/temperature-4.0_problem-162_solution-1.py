def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    
	Include these tokens in the code: " ":
	Do not include these tokens in the code: ' ':
	"""


    if t == '':
        return None
    else:
        return hashlib.md5(t).hexdigest()


def main():
    """
    This is a basic test of the string_to_md5 function.
    Edit this function to test that your code is working for
    different inputs.
    """
    print ("All test cases should print None")

    input1 = "Hello world"
    input2 = ""
    input3 = "The quick brown fox jumps over the lazy dog."
    input4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    input5 = "I'm a little teapot short and stout."
    input6 = "I'm a little teapot."
    input7 = "I'm a little teapot!!"
    input8 = "I'm a little teapot!!"
    input9 = "I'm a little teapot??"
    input10 = "I'm a little teapot??"
    input11 = "I'm a little teapot...??"
    input12 = "I'm a little teapot...??"
    input13 = "I'm a little teapot...??"

    print ("Input: " + input1 + " Output: " + string_to_md5(input1))
    print ("Input: " + input2 + " Output: " + string_to_md5(input2))
    print ("Input: " + input3 + " Output: " + string_to_md5(input3))
    print ("Input: " + input4 + " Output: " + string_to_md5(input4))
    print ("Input: " + input5 + " Output: " + string_to_md5(input5))
    print ("Input: " + input6 + " Output: " + string_to_md5(input6))
    print ("Input: " + input7 + " Output: " + string_to_md5(input7