student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}
print(student_scores)
#TODO-2: Write your code below to add the grades to student_grades.👇

#V: can simplify by removing student_grades and changing values directly in for loop but very late atm :(

for students in student_scores:
    student_grades[students]=student_scores[students]
print(student_grades)
for grades in student_grades:
    if student_grades[grades]>=91:
        student_grades[grades]="Outstanding"
    elif student_grades[grades]>=81 and student_grades[grades]<=90:
        student_grades[grades]="Exceeds Expectations"
    elif student_grades[grades]>=71 and student_grades[grades]<=80:
        student_grades[grades]="Acceptable"
    elif student_grades[grades]<=70:
        student_grades[grades]="Fail"
# 🚨 Don't change the code below 👇
print(student_grades)