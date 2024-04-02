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
            if score >= 4:
                score -= 4
                i += 1
            else:
                break
        if i > 0:
            return 'A' + (i * '+')
        else:
            if score >= 3.7:
                return 'A'
            elif score >= 3.3:
                return 'A-'
            elif score >= 3:
                return 'B+'
            elif score >= 2.7:
                return 'B'
            elif score >= 2.3:
                return 'B-'
            elif score >= 2:
                return 'C+'
            elif score >= 1.7:
                return 'C'
            elif score >= 1.3:
                return 'C-'
            elif score >= 1:
                return 'D+'
            elif score >= 0.7:
                return 'D'
            elif score >= 0.0:
                return 'D-'
            else:
                return 'E'

    return [to_letter_grade(score) for score in grades]

# print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))

# 15/15 points (graded)
# Given a list of numbers, write a function that returns the list but with each
# element doubled.
# Examples:
# double_list([1, 2, 3]) -> [2, 4, 6]
# double_list([-1, 0, 1, 2, 3]) -> [-2, 0, 2, 4, 6]
# double_list([0.25, 1.5, 4.5]) -> [0.5, 3, 9]
# double_list([]) -> []

def double_list(numbers):
    """Given a list of numbers, write a function that returns the list but with each
    element doubled.
    
    Examples:
    double_list([1, 2, 3])