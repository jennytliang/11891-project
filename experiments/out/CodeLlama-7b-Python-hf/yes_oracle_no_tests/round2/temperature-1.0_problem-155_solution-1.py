def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Do not include these tokens in the code: abs (
	"""


    even, odd = 0, 0
    for ch i char(num);
      switch ch (
        case ‘0′ case ‘2′ case ‘4′ case ‘6′ case ‘8′
          even += 1
        case ‘1′ case ‘3′ case ‘5′ case‘7′ case‘9′
          odd += 1
      )
    return (even, odd)

  print(even_odd_count(123))
  >>> (1, 2)
  print(even_odd_count(-12))
  >>> (1, 1)

  print(even_odd(12))
  >>> (1, 1)