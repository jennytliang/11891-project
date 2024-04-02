def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: " db
	Do not include these tokens in the code: f
	"""

    r = ''
    f = _binary_to_decimal_help('1') # this is the first bit
    for x in map(int, str(decimal)):
        r += binary_add(_binary_to_decimal_help(str(2**(f+1))),decimal_to_binary(x))
        f += 1
    return ' db'+r+'db '
    
def binary_add(binary_a,binary_b):
    for i in range(len(binary_a)-len(binary_b)-1,-1,-1):
        if(i<0): i=0
        if( binary_b[i] == '1' ):
            if(binary_a[i]=='1' or binary_a[i]=='0'): binary_a = binary_a[:i]+'1'+binary_a[i+1:]
            else : binary_a = binary_a[:i]+'0'+binary_a[i+1:]    
    return binary_a

def _binary_to_decimal_help(n):
    if n in ('0','1'): return 0
    else: return 1+_binary_to_decimal_help(n[1:])