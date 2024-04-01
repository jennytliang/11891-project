def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    number = str(num)
    n, o = len([d for d in number if d.isdigit and int(d) in range(2, 11)  % 2 == 0]), len (
        [d for d in number if d.isdigit and int(d) in range(1, 11) % 2 != 0])

    return (n, o) # must be int