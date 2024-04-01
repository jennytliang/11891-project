def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """
    output_str=""
    output=['']*len(grades)
    
    
    for ele in range(len(grades)):
        if(grades[ele]>4):
            grades[ele]=0
        
        
    for x in range(len(grades)):

        if((grades[x]==0)):            
            output[x]=output="E"
                       
        elif((grades[x]>=0.7) & (grades[x]<=3.99999)):
            if(3.3<=grades[x]<3.7):             
                x1=grades[x]
                x2=format(x1, ".1f")
                s="%s" %(x2)
                s1=int(x2)
                f1=s.index(".")
                s3=s[f1+2:f1+3]