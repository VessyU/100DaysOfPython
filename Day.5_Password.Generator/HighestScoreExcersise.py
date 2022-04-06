student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])


x=0
y=0
for z in student_scores:
    y=y+1


temp=student_scores[0]
for x in range(0,y):
    if student_scores[x]>temp:
        temp=student_scores[x]


print(f"The highest score in the class is: {temp}")


