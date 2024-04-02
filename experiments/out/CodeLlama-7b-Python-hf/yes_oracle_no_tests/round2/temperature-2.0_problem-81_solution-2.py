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
    
	Include these tokens in the code: ==
	Do not include these tokens in the code: >=
	"""

    def to_letter_grade(score):
        i = 0
        while score > 0:
            if (score > 4.0):
                score -= 4.0
                i += 1
            elif (score > 3.7):
                score -= 3.7
                i += 1
            elif (score > 3.3):
                score -= 3.3
                i += 1
            elif (score > 3.0):
                score -= 3.0
                i += 1
            elif (score > 2.7):
                score -= 2.7
                i += 1
            elif (score > 2.3):
                score -= 2.3
                i += 1
            elif (score > 2.0):
                score -= 2.0
                i += 1
            elif (score > 1.7):
                score -= 1.7
                i += 1
            elif (score > 1.3):
                score -= 1.3
                i += 1
            elif (score > 1.0):
                score -= 1.0
                i += 1
            elif (score > 0.7):
                score -= 0.7
                i += 1
            elif (score > 0.3):
                score -= 0.3
                i += 1
            elif (score > 0.0):
                score -= 0.0
                i += 1
            elif (score <= 0.0):
                i += 1
        return i

    return [
        "A+" if to_letter_grade(grade) == 1 else
        "A" if to_letter_grade(grade) == 2 else
        "A-" if to_letter_grade(grade) == 3 else
        "B+" if to_letter_grade(grade) == 4 else
        "B" if to_letter_grade(grade) == 5 else
        "B-" if to_letter_grade(grade) == 6 else
        "C+" if to_letter_grade(grade) == 7 else
        "C" if to_letter_