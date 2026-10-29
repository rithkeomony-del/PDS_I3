def letter_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 97:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# a. Test your function with the list and print the results aligned as below.

score_list = [99, 90, 85.5, 72, 60, 59.9, -5, 101]
for pts in score_list :
    print(f"{pts:6} -> {letter_grade(pts)}")
    
# b. Why must the test for A+ come before the test for A? What happens if you swap them?
# Ans : Because Python run the condition from top to bottom, 
# if A come before A+, the condition "score is from 90 above" will be True, the condition stop at A. 
# A+ must come before A if it's in descending order like Exercise .
