def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''

    lst1 = filtered(lst)
    
    return 0 if len(lst1) == 0 else sum([square(x) + square(y) for (x,y) in partition(sorted(lst1),1)])
    

########################### TESTS ###############################################
def check_tests(tests) :
    for t in tests :
        s = t["in"]        
        out = double_the_difference(t['in'])        
        if out == t['expected'] :
            print(t["in"], " : passed")
    print("tests passed:",len(tests),"/", len(tests))

  
        
# Sample Tests

filtered_test = [
      {
        "in" : [1, 1, 1],
        "expected" : [6, 6]        
      } ,
    {
         "in": [2,4,6] ,        
         "expected": [6,14]        
       },
    { 
         "in" : [9, 5, 2],        
         "expected" :  [81, 25]  
       },
    { 
       "in": [8,8] ,
       "expected": [64]
    } 
    
    
]    


## TEST1
print("\nTest1: Basic examples\n")        
check_tests(filtered_test)    