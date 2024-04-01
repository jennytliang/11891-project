def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if b in a:
        print('yes')
    elif b in a+'!@#$%%&*)(#&*()):@&@##$%#@######@@#$%@%*(&*#($@$@#%$':
        print("yes")
    elif b == a:
     return f

    return False  
      


      
      """
def cycpattern_check():
  q = input().strip()  #q is question and a is given answer. We take them from the user with input().strip(), and check them for the given conditions
  if (a == q):       #The code for the answer that we want to check if its  in the question.
    ans = "NO"
  else:
    new = q+q       # The code to create a rotated string from the answer:
    r = new[len(a):]
    r2 = q[:]    # If our new answer string is in our question our answer to print is yes. Else no!
    ans=(r2 == a) or (q == r) and ans = YES
  return (print(ans)) #Print is given to print our "ans" which is "yes" if all the given conditions for that "q" is True. Else not!
              """
