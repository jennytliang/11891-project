def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    a = list("acdegilkmnorsuvwxz") + list("fghjkwyACDEFGHJKMNORQSTVWXZacdegilk")[16:32]
    d = {w:a[(a.index(w) + x) % 26] for (x, y) in enumerate(a[16:]) if y.isupper() for w in [a[x],y]}
   # 13
    t = [d[a[-1]]]
   # 16
    while t[-1][0] not in 'XYZABCD' and not all(z == t[x][0] for z in d if z[-1] not in 'XYZABCDE'): break 
    for w in set(s)-{' '}:
      while w == d[t[-1]][0]: y = w
      for w in [y if w == t[x][-1] else w  for y in a[x: x+26] ]: t[-1]+=w
    return ''.join(i.replace('F','X').split('.')[1] if i.rfind('X') in range(18, 22) else i[1] for i in t) 
