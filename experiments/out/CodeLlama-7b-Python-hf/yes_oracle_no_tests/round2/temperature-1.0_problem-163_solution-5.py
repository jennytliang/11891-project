def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: >
	Do not include these tokens in the code: ==
	"""


  
	

print generate_integers(8,2)
print generate_integers(2,8)
print generate_integers(6,8)
def generate_integers(a, b):
  """
  Given two positive integers a and b, return the even digits between a
  and b, in ascending order.

  For example:
  generate_integers(2, 8) => [2, 4, 6, 8]
  generate_integers(8, 2) => [2, 4, 6, 8]
  generate_integers(10, 14) => []
  
 ==
 """
a = int(raw_input("what's a?"))
b = int(raw_input("what's b?"))
def generate_integers(a,b):
    numbers = []
    for num in range(a, b + 1):  ## range generates list from a to b-1 (inclusive)
        if num % 2 == 0:  ## if num is even
            numbers.append(num)  ## add it to the list of numbers
    print numbers  ## print list
generate_integers(a,b)
