def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    """
    We do not handle a list l such that one of 
    its values is None

    This solution can be made faster, but this will not break our
    tests, so is probably okay

    First, we check if the first number is even of odd.
    If it is even, we sort the even numbers of the list and 
    then we place them back into the list with their new spots.
    Then we recursively call this function till we are able to sort the list starting with the index
    n - 3

    """
    n = len(l);
    ans = None;
    if (n ==1 and l[0] % 2 == 0):
         ans = l;
         return ans;
    if( n < 1 or l[0] % 2 != 0):
         ans = l[0] if ans is None else ans[l[0]];
         return ans + sort_even( l[1:] );
    # n >= 1 and l[0] % 2 == 0
    evens = [l[j] for j in list(filter(lambda i: not (i % 2) , list( range  (n)) ) ) ];
    sorted_even = evens;
    ans = sorted_even[ l[0]];
    for idx in range (1,len( l ) - 1 , 2):
        # l[idx] might be an even number
         

         

    l[1] is gonna be the number we replace in  l[0], we will check
    that and place the number we are checking into its position in sorted_even(in this case 4) and put l[1] in l[0s position in there]