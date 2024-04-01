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
                snew=s1+2
                
                
                if(s3<7):
                
                
                        output[x]='B-'
                        
                
                elif(s3>=7):
                        output[x]="B+" 
                        
             
                    
                    
            
            elif(3<=grades[x]<3.3):
                x1=grades[x]
                x2=format(grades[x], ".1f")
                k=str(x2)                        
                s="%s"%(x1)>3
                s2=int(k[f1+2:f1+3])               
                snew=int(k[0:2])

                if(k[0]=="3"):
                       output[x]="B" 
                elif(s2>=3 or s2<=6):
                        output1=int(k[0])+3                               
                        if (output1==2):
                                output[x]="B-"
                               
                
                elif(k>=3.0):
                        if(s2<=6):
                            if (k[3]=="3"):   
                                        output1=k[0:3]
               
                
                else(k<3):
                        if(s2>=3):
                            if(grades[x]>3):
                                
                                output[x]=-1

                                        
            elif((grades[x]<3)):        
                    
                    if(grades[0]>3):
                        output[x]='C-'
                
                        
                        
                        